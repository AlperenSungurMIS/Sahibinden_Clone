from rest_framework import serializers
from category.models import Ev, Araba

class EvSerializer(serializers.ModelSerializer):
    # ImageField otomatik olarak işlenir
   # images = serializers.ImageField(required=False)  # Opsiyonel hale getirmek için required=False ekledik

    class Meta:
        model = Ev
        fields = "__all__"  # Tüm alanlar dahil edilir


class ArabaSerializer(serializers.ModelSerializer):
    # ImageField otomatik olarak işlenir
    #images = serializers.ImageField(required=False)  # Opsiyonel hale getirmek için required=False ekledik

    class Meta:
        model = Araba
        fields = "__all__"  # Tüm alanlar dahil edilir
