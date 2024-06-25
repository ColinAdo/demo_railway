from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'author', 
        'title', 
        'created_at', 
    ]

admin.site.register(Post, PostAdmin)
