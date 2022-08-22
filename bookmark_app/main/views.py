from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bookmarks, Tag
from .forms import BookmarksForm, TagForm

# Create your views here.
def overview(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  tags = Tag.objects.all()
  bookmarks = Bookmarks.objects.filter(tags__name__icontains=q)
  return render(request, 'main/overview.html', {'bookmarks':bookmarks, 'tags': tags})

def add(request):
  form = BookmarksForm()
  if request.method == 'POST':
    form = BookmarksForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('overview')
  return render(request, 'main/bookmark-form.html', {'form': form})

def add_tag(request):
  form = TagForm()
  if request.method == 'POST':
    form = TagForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('overview')
  return render(request, 'main/tag-form.html', {'form': form})

def update(request, id):
  bookmark = Bookmarks.objects.get(id=id)
  form = BookmarksForm(instance=bookmark)

  if request.method == 'POST':
    form = BookmarksForm(request.POST, instance=bookmark)
    if form.is_valid():
      form.save()
      return redirect('overview')
    else:
      return redirect('overview')
  return render(request, 'main/bookmark-form.html', {'form': form})

def delete(request, id):
  bookmark = Bookmarks.objects.get(id=id)
  if request.method == 'POST':
    bookmark.delete()
    return redirect('overview')
  return render(request, 'main/delete.html', {'obj': bookmark})

