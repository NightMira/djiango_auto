from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'plate', 'year', 'user')
    search_fields = ('brand', 'model', 'plate', 'vin')
    list_filter = ('brand', 'year')