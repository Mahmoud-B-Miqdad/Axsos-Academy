from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Show

def root_redirect(request):
    return redirect('/shows')

def index(request):
    return render(request, 'index.html', {'shows': Show.objects.all()})

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    if request.method == "POST":
        errors = Show.objects.validate_show(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        
        # Delegating creation logic to the Fat Model
        new_show = Show.objects.create_show(request.POST)
        return redirect(f'/shows/{new_show.id}')

def show_detail(request, show_id):
    return render(request, 'show_detail.html', {'show': get_object_or_404(Show, id=show_id)})

def edit_show(request, show_id):
    return render(request, 'edit_show.html', {'show': get_object_or_404(Show, id=show_id)})

def update_show(request, show_id):
    if request.method == "POST":
        errors = Show.objects.validate_show(request.POST, is_update=True, show_id=show_id)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
        
        # Delegating update logic to the Fat Model
        show = Show.objects.update_show(show_id, request.POST)
        return redirect(f'/shows/{show.id}')

def destroy_show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    show.delete()
    return redirect('/shows')

def validate_ajax(request):
    """Skinny view endpoint for asynchronous Sensei Bonus validations"""
    is_update = request.GET.get('is_update', 'false') == 'true'
    show_id = request.GET.get('show_id', None)
    
    errors = Show.objects.validate_show(request.GET, is_update=is_update, show_id=show_id)
    
    if errors:
        return JsonResponse({'valid': False, 'errors': errors})
    return JsonResponse({'valid': True})