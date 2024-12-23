from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from category.models import Araba, Ev
from .serializers import EvSerializer, ArabaSerializer

class ListingAPIView(APIView):
    def get(self, request):
        ev = Ev.objects.all()
        araba = Araba.objects.all()

        ev_serializer = EvSerializer(ev, many=True)
        araba_serializer = ArabaSerializer(araba, many=True)

        return Response({
            "ev": ev_serializer.data,
            "araba": araba_serializer.data
        }, status = status.HTTP_200_OK)


"""
    def post(self, request):
        title = request.data.get("title")
        description = request.data.get("description")
        price = request.data.get("price")
        category = request.data.get("category")

        listing = Listing.objects.create(
            title=title, description=description, price=price, category=category
        )
        return Response({"message": "İlan başarıyla oluşturuldu!", "listing_id": listing.id}, status=status.HTTP_201_CREATED)
"""