from django.contrib import admin
from .models import Restaurant, Reviews


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Reviews)
