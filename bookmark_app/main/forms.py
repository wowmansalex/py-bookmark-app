from django.forms import ModelForm
from .models import Bookmarks, Tag

class BookmarksForm(ModelForm):
  class Meta:
    model = Bookmarks
    fields = '__all__'

class TagForm(ModelForm):
  class Meta:
    model = Tag
    fields = '__all__'