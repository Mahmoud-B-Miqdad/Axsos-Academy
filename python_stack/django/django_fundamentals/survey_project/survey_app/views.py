from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        print(request.POST)
        
        name = request.POST.get('name')
        location = request.POST.get('location')
        language = request.POST.get('language')
        bootcamp_type = request.POST.get('bootcamp_type')
        
        interests_list = request.POST.getlist('interests')
        interests = ", ".join(interests_list) if interests_list else "None Selected"
        
        comment = request.POST.get('comment', 'No comment provided.')

        context = {
            "context_name": name,
            "context_location": location,
            "context_language": language,
            "context_bootcamp_type": bootcamp_type,
            "context_interests": interests,
            "context_comment": comment
        }
        return render(request, 'result.html', context)
    
    return redirect('/')