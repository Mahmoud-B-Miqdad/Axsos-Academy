from django.shortcuts import render, redirect
import random

def index(request):
    if 'target_number' not in request.session:
        request.session['target_number'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['message'] = None
        request.session['game_over'] = False
    return render(request, 'index.html')

def guess(request):
    if request.session['game_over']:
        return redirect('index')
    guess = int(request.POST['guess'])
    request.session['attempts'] += 1
    if guess < request.session['target_number']:
        request.session['message'] = "Too low!"
        request.session['color'] = "bg-danger"
    elif guess > request.session['target_number']:
        request.session['message'] = "Too high!"
        request.session['color'] = "bg-danger"
    else:
        request.session['message'] = f"{request.session['target_number']} was the number!"
        request.session['color'] = "bg-success"
        request.session['game_over'] = True

    if request.session['attempts'] >= 5 and not request.session['game_over']:
        request.session['message'] = "You Lose! Game Over."
        request.session['color'] = "bg-danger"
        request.session['game_over'] = True

    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')