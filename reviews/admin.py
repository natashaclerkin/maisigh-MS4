from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'review_title',
        'user_profile',
        'created_on',
    )

    list_filter = ("product",)
    search_fields = ['product', 'review_title', 'review_content']


admin.site.register(Review, ReviewAdmin)
