from django.db import models


__all__ = ["User"]


# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField()
    house_no = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        db_table = "User"
