from django.contrib import admin

# Register your models here.
from .models import Bookmarks, Tag

admin.site.register(Bookmarks)
admin.site.register(Tag)