from django.db import models

class Listing(models.Model):
    CATEGORY_CHOICES = [
        ('real_estate', 'Emlak'),
        ('car', 'Araba'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    # Emlak
    rooms = models.IntegerField(null=True, blank=True)  # Oda sayısı
    area = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)  # Metrekare

    # Araba
    make = models.CharField(max_length=50, null=True, blank=True)  # Marka
    model = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)  # Model yılı
    mileage = models.IntegerField(null=True, blank=True)  # Kilometre

    def __str__(self):
        return f"{self.title} - {self.category}"
