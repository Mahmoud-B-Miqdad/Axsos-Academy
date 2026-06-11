from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Course, Comment

def index(request):
    """Renders the main wireframe listing all courses."""
    context = {'courses': Course.objects.all()}
    return render(request, 'index.html', context)

def create_course(request):
    """Handles core server-side validation and course creation."""
    if request.method == "POST":
        errors = Course.objects.validate_course(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Course.objects.create_course_with_desc(request.POST)
    return redirect('/')

def destroy_course(request, course_id):
    """Traditional remove/confirmation route (Fallback if AJAX is not used)."""
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        return redirect('/')
    return render(request, 'delete_confirm.html', {'course': course})

def delete_course_ajax(request, course_id):
    """Sensei Bonus: Asynchronously deletes a course via AJAX."""
    if request.method == "POST":
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def course_comments(request, course_id):
    """Ninja Bonus: Renders and processes the comments page for a course."""
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        comment_content = request.POST.get('comment', '').strip()
        if comment_content:
            Comment.objects.create(content=comment_content, course=course)
        return redirect(f'/courses/{course_id}/comments/')
        
    return render(request, 'comments.html', {'course': course})