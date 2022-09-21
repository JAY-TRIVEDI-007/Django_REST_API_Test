from django.db import models
from users.models import User

__all__ = ["Ads", "Post"]


# Create your models here.
class Ads(models.Model):
    adID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "Ad"


class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    adID = models.ForeignKey(Ads, on_delete=models.CASCADE)

    class Meta:
        db_table = "Post"
