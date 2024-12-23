from django.db import models
from advert.models import Advert

class Araba(Advert):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    yil = models.PositiveIntegerField()
    kilometre = models.PositiveIntegerField()
    renk = models.CharField(max_length=30)
    motor_hacmi = models.PositiveIntegerField()
    yakit_turu = models.CharField(max_length=20, choices=[
        ('Benzin', 'Benzin'),
        ('Dizel', 'Dizel'),
        ('Elektrik', 'Elektrik'),
        ('Hibrit', 'Hibrit'),
    ])
    vites_turu = models.CharField(max_length=20, choices=[
        ('Manuel', 'Manuel'),
        ('Otomatik', 'Otomatik'),
        ('Yarı Otomatik', 'Yarı Otomatik'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.marka} {self.model} ({self.yil})"


class Ev(Advert):
    oda_sayisi = models.PositiveIntegerField()
    metrekare = models.PositiveIntegerField()
    kat = models.PositiveIntegerField()
    bina_yasi = models.PositiveIntegerField()
    isinma_tipi = models.CharField(max_length=20, choices=[
        ('Doğalgaz', 'Doğalgaz'),
        ('Elektrik', 'Elektrik'),
        ('Soba', 'Soba'),
        ('Merkezi', 'Merkezi'),
    ])
    balkon = models.BooleanField(default=False)
    adres = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.oda_sayisi} oda, {self.metrekare} m²"
