from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'body', 'created_at', 'update_at')
    list_display_links = ('id', 'author')
    search_fields = ('author', 'title')


admin.site.register(Post, PostAdmin)
