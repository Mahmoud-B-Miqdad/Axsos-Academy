from django.shortcuts import render, redirect

def index(request):
    if 'visits' not in request.session:
        request.session['visits'] = 0

    if 'counter' not in request.session:
        request.session['counter'] = 0
    
    request.session['visits'] += 1
    return render(request, 'index.html')

def plus_two(request):
    request.session['counter'] += 2
    return redirect('/')

def custom_increment(request):
    if request.method == "POST":
        increment_by = int(request.POST.get('increment_by', 1))
        
        request.session['counter'] += (increment_by)
            
    return redirect('/')

def destroy_session(request):
    if 'counter' in request.session:
        del request.session['counter']
    if 'visits' in request.session:
        del request.session['visits']
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    
    return redirect('/')