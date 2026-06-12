from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import User
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
                return redirect('/success')
        
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