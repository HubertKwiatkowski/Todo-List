from django.contrib import admin

from .models import *

admin.site.register(ListItem)
admin.site.register(Tag)
admin.site.register(Status)