from django.db import models
from users.models import User

__all__ = ["Car", "Owner"]


# Create your models here.
class Car(models.Model):
    carID = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    number_plate = models.CharField(max_length=255)

    class Meta:
        db_table = "Car"


class Owner(models.Model):
    ownerID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    carID = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        db_table = "Owner"
