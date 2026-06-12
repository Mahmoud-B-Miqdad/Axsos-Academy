import re
import bcrypt
from django.db import models
from datetime import date

class UserManager(models.Manager):
    def register_validator(self, post_data):
        """
        Handles all server-side validation for user registration.
        Includes age verification (COPPA - 13 years old) and email uniqueness.
        """
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$')
        
        # Name validation
        if len(post_data.get('first_name', '')) < 2 or not post_data.get('first_name', '').isalpha():
            errors['first_name'] = "First name must be at least 2 characters long and contain letters only."
            
        if len(post_data.get('last_name', '')) < 2 or not post_data.get('last_name', '').isalpha():
            errors['last_name'] = "Last name must be at least 2 characters long and contain letters only."
            
        # Email validation
        email = post_data.get('email', '')
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Invalid email address format."
        elif self.filter(email=email).exists():
            errors['email'] = "This email address is already registered."

        # Birthday & Age validation (Sensei Bonus: COPPA compliance)
        birthday_str = post_data.get('birthday', '')
        if not birthday_str:
            errors['birthday'] = "Date of birth is required."
        else:
            try:
                birth_date = date.fromisoformat(birthday_str)
                today = date.today()
                
                # Calculate age accurately
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                
                if birth_date >= today:
                    errors['birthday'] = "Birth date must be a date in the past."
                elif age < 13:
                    errors['birthday'] = "You must be at least 13 years old to register."
            except ValueError:
                errors['birthday'] = "Invalid date format."

        # Password validation
        password = post_data.get('password', '')
        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        if password != post_data.get('confirm_password', ''):
            errors['confirm_password'] = "Passwords do not match."
            
        return errors
    
    def register_user(self, post_data):
        """
        Fat Model Behavior: Handles password hashing and database insertion 
        completely away from the view layer.
        """
        # 1. Hash the password securely inside the model
        hashed_pw = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt()).decode()
        
        # 2. Create and return the user object
        return self.create(
            first_name=post_data['first_name'],
            last_name=post_data['last_name'],
            email=post_data['email'],
            birthday=post_data['birthday'],
            password=hashed_pw
        )

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    password = models.CharField(max_length=255) # Capable of storing secure Bcrypt hashes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Hook up the custom Fat Model manager
    objects = UserManager()


class BookManager(models.Manager):
    def book_validator(self, post_data):
        """Validates book creation and modifications input parameters."""
        errors = {}
        if len(post_data.get('title', '').strip()) < 1:
            errors['title'] = "Book title is required!"
        if len(post_data.get('description', '').strip()) < 5:
            errors['description'] = "Description must be at least 5 characters long!"
        return errors

    def create_book(self, post_data, user_obj):
        """
        Fat Model Pattern: Handles direct instance database row insertion
        and associates the creator inside the Many-to-Many favorite relationship.
        """
        new_book = self.create(
            title=post_data['title'],
            description=post_data['description'],
            uploaded_by=user_obj 
        )
        # Add to current user's favorite stack using the correct forward relation
        new_book.users_who_like.add(user_obj) 
        return new_book

    def update_book(self, post_data, book_id, user_id):
        """
        Fat Model Pattern: Encapsulates ownership confirmation checks 
        and updates the object row state inside the database table.
        """
        try:
            book_to_edit = self.get(id=book_id)
            # Authorization barrier control check
            if book_to_edit.uploaded_by.id == user_id:
                book_to_edit.title = post_data['title']
                book_to_edit.description = post_data['description']
                book_to_edit.save()
                return True, "Book updated successfully!"
            return False, "Unauthorized action! You do not own this book record."
        except self.model.DoesNotExist:
            return False, "The targeted book record does not exist."


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    # Relationships definition setup
    uploaded_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name="books_uploaded")
    users_who_like = models.ManyToManyField('User', related_name="liked_books")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Custom manager attachment link
    objects = BookManager()