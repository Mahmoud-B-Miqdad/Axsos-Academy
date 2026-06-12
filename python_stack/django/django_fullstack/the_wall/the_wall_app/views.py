from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from .models import User, Message, Comment
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
                return redirect('/wall')
        
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

def can_delete_message(message_obj):
    time_elapsed = timezone.now() - message_obj.created_at
    minutes_elapsed = time_elapsed.total_seconds() / 60
    return minutes_elapsed <= 30

def wall_index(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in first to access the wall.")
        return redirect('/')
        
    current_user = User.objects.get(id=request.session['user_id'])
    all_messages = Message.objects.all().order_by('-created_at')
    
    for msg in all_messages:
        msg.is_deletable = (msg.user.id == current_user.id) and can_delete_message(msg)

    context = {
        "user": current_user,
        "all_messages": all_messages
    }
    return render(request, 'wall.html', context)

def create_message(request):
    if request.method == "POST":
        errors = Message.objects.message_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wall')
            
        current_user = User.objects.get(id=request.session['user_id'])
        Message.objects.post_message(request.POST, current_user)
        messages.success(request, "Your message has been posted successfully!")
    return redirect('/wall')

def create_comment(request):
    if request.method == "POST":
        errors = Comment.objects.comment_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wall')
            
        current_user = User.objects.get(id=request.session['user_id'])
        target_message = Message.objects.get(id=request.POST['message_id'])
        Comment.objects.post_comment(request.POST, current_user, target_message)
        messages.success(request, "Comment added successfully!")
    return redirect('/wall')

def delete_message(request, message_id):
    try:
        message_to_delete = Message.objects.get(id=message_id)
        if message_to_delete.user.id == request.session.get('user_id'):
            if can_delete_message(message_to_delete):
                message_to_delete.delete()
                messages.success(request, "Message deleted successfully.")
            else:
                messages.error(request, "You cannot delete messages older than 30 minutes!")
        else:
            messages.error(request, "Unauthorized action!")
    except Message.DoesNotExist:
        messages.error(request, "Message not found.")
        
    return redirect('/wall')