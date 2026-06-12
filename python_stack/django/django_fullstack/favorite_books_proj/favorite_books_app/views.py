from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import *
import bcrypt

def index(request):
    """Renders the main authentication landing page."""
    return render(request, 'auth.html')

def register(request):
    """Delegates validation to the model, hashes password, and creates user."""
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        # Create and hash inside the Fat Model (without logging them into session)
        User.objects.register_user(request.POST)
        
        # Add a success flash message for the user
        messages.success(request, "Registration successful! Please sign in with your new credentials.")
        
        # Redirect back to the login page view instead of /success
        return redirect('/')
        
    return redirect('/')

def login(request):
    """Processes login attempts with safe database fetching and encryption checks."""
    if request.method == "POST":
        # Using filter() to cleanly check existence without crashing on non-existent records
        users = User.objects.filter(email=request.POST['email'])
        if users:
            logged_user = users[0]
            # Match secure passwords
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                request.session['user_name'] = f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('/books')
        
        # Generic error message to prevent account harvesting vulnerabilities
        messages.error(request, "Invalid email or password credentials.")
    return redirect('/')

def success(request):
    """Route Protection: Prevents unauthenticated users from forcing entry."""
    if 'user_id' not in request.session:
        messages.error(request, "Authentication required. Please sign in first.")
        return redirect('/')
    return render(request, 'success.html')

def logout(request):
    """Completely flushes the current session, wiping user state."""
    request.session.flush()
    return redirect('/')

def check_email(request):
    """Sensei Bonus: Dynamic backend endpoint for live AJAX email availability checking."""
    email = request.GET.get('email', None)
    data = {
        'exists': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

def books_index(request):
    """Skinny View: Validates active user state session and renders the primary dashboard."""
    if 'user_id' not in request.session:
        messages.error(request, "Please log in first to access the dashboard.")
        return redirect('/')
        
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_books": Book.objects.all().order_by('-created_at')
    }
    return render(request, 'books.html', context)


def add_book(request):
    """Skinny View: Offloads validation checks and data initialization processing to the model layer."""
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books')
            
        current_user = User.objects.get(id=request.session['user_id'])
        Book.objects.create_book(request.POST, current_user)
        messages.success(request, "Book added and added to your favorites successfully!")
    return redirect('/books')


def book_detail(request, book_id):
    """Skinny View: Pulls context information data safely to present the record specification workspace."""
    if 'user_id' not in request.session:
        return redirect('/')
        
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        messages.error(request, "Book not found.")
        return redirect('/books')
        
    current_user = User.objects.get(id=request.session['user_id'])
    
    context = {
        "user": current_user,
        "book": book,
        "is_favorited": current_user in book.users_who_like.all()
    }
    return render(request, 'book_detail.html', context)


def update_book(request, book_id):
    """Skinny View: Passes payload mapping parameters into the manager logic layer."""
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/books/{book_id}')
            
        # Triggers database update logic directly from the Model Layer
        success, system_message = Book.objects.update_book(
            request.POST, 
            book_id, 
            request.session['user_id']
        )
        
        if success:
            messages.success(request, system_message)
        else:
            messages.error(request, system_message)
            
    return redirect(f'/books/{book_id}')


def delete_book(request, book_id):
    """Skinny View: Destroys targeted rows conditionally based on standard ownership security guidelines."""
    if 'user_id' not in request.session:
        return redirect('/')
        
    try:
        book = Book.objects.get(id=book_id)
        if book.uploaded_by.id == request.session['user_id']:
            book.delete()
            messages.success(request, "Book removed from the system.")
        else:
            messages.error(request, "Unauthorized request attempt.")
    except Book.DoesNotExist:
        messages.error(request, "Targeted book cannot be discovered.")
        
    return redirect('/books')


def toggle_favorite(request, book_id, action):
    """Skinny View: Processes safe attachment and detachment configuration switches inside M2M relation maps."""
    if 'user_id' not in request.session:
        return redirect('/')
        
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    
    if action == "add":
        book.users_who_like.add(user)
        messages.success(request, f"Added '{book.title}' to your favorites.")
    elif action == "remove":
        book.users_who_like.remove(user)
        messages.success(request, f"Removed '{book.title}' from your favorites.")
        
    return redirect(request.META.get('HTTP_REFERER', '/books'))


def my_favorites(request):
    """Skinny View: Pulls filtered view constraints safely using native ORM related targets."""
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'my_favorites.html', context)