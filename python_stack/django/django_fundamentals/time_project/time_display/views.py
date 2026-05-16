from django.shortcuts import render
from datetime import datetime

def index(request):
    now = datetime.now()
    
    context = {
        "date_string": now.strftime("%b %d, %Y"),
        "time_string": now.strftime("%I:%M %p")
    }
    return render(request, 'index.html', context)