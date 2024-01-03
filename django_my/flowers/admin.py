from django.contrib import admin
from .models import Articles
from .models import orchids


admin.site.register(orchids)

class Articl_admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    search_fields = ('name',)


admin.site.register(Articles, Articl_admin)