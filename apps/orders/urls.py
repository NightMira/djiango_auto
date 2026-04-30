from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:service_id>/', views.add_to_order, name='add_to_order'),
    path('cart/', views.cart_view, name='cart'),
]