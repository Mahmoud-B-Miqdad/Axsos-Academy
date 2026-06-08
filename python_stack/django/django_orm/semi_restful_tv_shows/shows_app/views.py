from django.shortcuts import render, redirect, get_object_or_404
from .models import Show

# 1. GET - /shows
def index(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "index.html", context)

# 2. GET - /shows/new
def new(request):
    return render(request, "new.html")

# 3. POST - /shows/create
def create(request):
    if request.method == "POST":
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            desc=request.POST['desc']
        )
        return redirect(f'/shows/{new_show.id}')
    return redirect('/shows')

# 4. GET - /shows/<id>
def show(request, show_id):
    context = {
        "show": get_object_or_404(Show, id=show_id)
    }
    return render(request, "show.html", context)

# 5. GET - /shows/<id>/edit
def edit(request, show_id):
    show_item = get_object_or_404(Show, id=show_id)
    formatted_date = show_item.release_date.strftime('%Y-%m-%d')
    context = {
        "show": show_item,
        "formatted_date": formatted_date
    }
    return render(request, "edit.html", context)

# 6. POST - /shows/<id>/update
def update(request, show_id):
    if request.method == "POST":
        show_item = get_object_or_404(Show, id=show_id)
        show_item.title = request.POST['title']
        show_item.network = request.POST['network']
        show_item.release_date = request.POST['release_date']
        show_item.desc = request.POST['desc']
        show_item.save()
        return redirect(f'/shows/{show_item.id}')
    return redirect('/shows')

# 7. /shows/<id>/destroy
def destroy(request, show_id):
    show_item = get_object_or_404(Show, id=show_id)
    show_item.delete()
    return redirect('/shows')