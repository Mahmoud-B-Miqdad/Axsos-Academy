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

class MessageManager(models.Manager):
    def message_validator(self, post_data):
        errors = {}
        if len(post_data['message_text'].strip()) < 1:
            errors['message_text'] = "Message post cannot be empty!"
        return errors

    def post_message(self, post_data, user_obj):
        """Fat Model implementation: Handles creation internally."""
        return self.create(
            message_text=post_data['message_text'],
            user=user_obj
        )

class Message(models.Model):
    message_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = MessageManager()


class CommentManager(models.Manager):
    def comment_validator(self, post_data):
        errors = {}
        if len(post_data['comment_text'].strip()) < 1:
            errors['comment_text'] = "Comment cannot be empty!"
        return errors

    def post_comment(self, post_data, user_obj, message_obj):
        """Fat Model implementation: Handles creation internally."""
        return self.create(
            comment_text=post_data['comment_text'],
            user=user_obj,
            message=message_obj
        )

class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CommentManager()