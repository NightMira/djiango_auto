from django.contrib import admin
from .models import Order, OrderService


class OrderServiceInline(admin.TabularInline):
    model = OrderService
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car', 'status', 'total_price')
    list_filter = ('status',)
    inlines = [OrderServiceInline]