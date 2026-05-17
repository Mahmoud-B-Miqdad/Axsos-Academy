from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['moves'] = 0
        request.session['game_over'] = False
        request.session['message'] = None\
        
    return render(request, 'index.html')

def process_money(request):
    if request.session.get('game_over'):
        return redirect('/')

    building = request.POST['building']
    
    building_config = {
        'farm': (10, 20),
        'cave': (5, 10),
        'house': (2, 5),
        'casino': (-50, 50)
    }

    if building in building_config:
        min_gold, max_gold = building_config[building]
        earned = random.randint(min_gold, max_gold)
        request.session['gold'] += earned
        request.session['moves'] += 1
        
        time_now = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        if earned >= 0:
            activity = {
                'class': 'text-success',
                'text': f"Earned {earned} golds from the {building}! ({time_now})"
            }
        else:
            activity = {
                'class': 'text-danger',
                'text': f"Entered a casino and lost {abs(earned)} golds... Ouch. ({time_now})"
            }
        
        request.session['activities'].insert(0, activity)

        if request.session['gold'] >= 500:
            request.session['game_over'] = True
            request.session['message'] = "WINNER! You reached 500 gold!"
        elif request.session['moves'] >= 15:
            request.session['game_over'] = True
            request.session['message'] = "GAME OVER! You ran out of moves."

    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')