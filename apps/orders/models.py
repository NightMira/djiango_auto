from django.db import models
from apps.core.models import BaseModel
from apps.users.models import User
from apps.cars.models import Car
from apps.services.models import Service  # создадим позже


class Order(BaseModel):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    employee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_orders'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class OrderService(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_services'
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    price_at_time = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.service.name} x{self.quantity}"