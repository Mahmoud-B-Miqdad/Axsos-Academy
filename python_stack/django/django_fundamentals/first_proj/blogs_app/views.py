from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse

# 1. Path / redirects to /blogs
def root(request):
    return redirect("/blogs")

# 2. The /blogs path displays text
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

# 3. The /blogs/new path displays the text of a new form
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

# 4. The /blogs/create path redirects to the main path /
def create(request):
    return redirect("/")

# 5. The /blogs/<number> path captures the number and displays it dynamically
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

# 6. The path /blogs/<number>/edit captures the number for editing purposes
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

# 7. The path /blogs/<number>/delete redirects to /blogs after deletion
def destroy(request, number):
    return redirect("/blogs")

# 8. The bonus path returns data in JSON format
def json_response(request):
    data = {
        "title": "My first blog",
        "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit."
    }
    return JsonResponse(data)