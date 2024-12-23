from django.db import models
from django.contrib.auth.models import User

class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adverts")  # default=1 ekledik
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title