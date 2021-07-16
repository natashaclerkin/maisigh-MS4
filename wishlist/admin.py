from django.contrib import admin
from wishlist.models import Wishlist, WishlistItem

# Register your models here.
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
