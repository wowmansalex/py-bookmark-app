from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Bookmarks, Tag
from .forms import BookmarksForm, TagForm

# Create your views here.
def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('overview')
    else:
      messages.error(request, 'User does not exist')

  return render(request, 'main/login_register.html')

def logoutUser(request):
  logout((request))
  return redirect('overview')


def overview(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  tags = Tag.objects.all()
  bookmarks = Bookmarks.objects.filter(
    Q(tags__name__icontains=q) |
    Q(title__icontains=q) |
    Q(url__contains=q)
    )
  bookmark_count = bookmarks.count()
  return render(request, 'main/overview.html', {'bookmarks':bookmarks, 'tags': tags, 'bookmark_count': bookmark_count})

@login_required(login_url='login')
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

