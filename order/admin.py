from django.contrib import admin
from .models import *

class ShopAdmin(admin.ModelAdmin):
    list_display = ['servis_name']

admin.site.register(Shop,ShopAdmin)



class StatusAdmin(admin.ModelAdmin):
    list_display = ['status_name']

admin.site.register(Status,StatusAdmin)


class PostAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Post._meta.fields]
    list_filter = ['shop', ]
    search_fields = ['author', 'shop', 'status', 'Klient']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
