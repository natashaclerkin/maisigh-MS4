from django.contrib import admin
from .models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_on',
        'status',
    )
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)
