from django.contrib import admin

from .models import ListItem, Tag

admin.site.register(ListItem)
admin.site.register(Tag)