from django.db import models
from apps.core.models import BaseModel
from apps.users.models import User


class Car(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cars'
    )

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    vin = models.CharField(max_length=50, unique=True)
    plate = models.CharField(max_length=20, unique=True)

    mileage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.plate})"