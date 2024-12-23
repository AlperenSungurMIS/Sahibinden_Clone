from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from category.models import Araba, Ev
from homepage.serializers import ArabaSerializer, EvSerializer
from rest_framework.exceptions import NotFound
from account.dec import jwt_required  # Dekoratörün tanımlı olduğu dosyadan import yapıyoruz


class ArabaAPIView(APIView):
    @jwt_required
    def get(self, request, pk=None):
        """
        Araba bilgilerini getirir. Eğer `pk` verilirse tek bir araba döner.
        """
        if pk:
            try:
                araba = Araba.objects.get(pk=pk)
            except Araba.DoesNotExist:
                raise NotFound("Araba bulunamadı.")
            serializer = ArabaSerializer(araba)
        else:
            arabalar = Araba.objects.all()
            serializer = ArabaSerializer(arabalar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @jwt_required
    def post(self, request):
        """
        Yeni bir araba ilanı oluşturur.
        """
        request.data["user"] = request.user.id
        serializer = ArabaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @jwt_required
    def put(self, request, pk):
        """
        Araba ilanını günceller.
        """
        try:
            araba = Araba.objects.get(pk=pk)
            if araba.user != request.user:  # Kullanıcı yetkilendirme kontrolü
                return Response({"error": "Bu ilanı güncelleme yetkiniz yok."}, status=status.HTTP_403_FORBIDDEN)
        except Araba.DoesNotExist:
            raise NotFound("Bu ilana erişiminiz yok veya ilan bulunamadı.")

        request.data["user"] = request.user.id
        serializer = ArabaSerializer(araba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @jwt_required
    def delete(self, request, pk):
        """
        Bir araba ilanını siler.
        """
        try:
            araba = Araba.objects.get(pk=pk)
            if araba.user != request.user:  # Kullanıcı yetkilendirme kontrolü
                return Response({"error": "Bu ilanı silme yetkiniz yok."}, status=status.HTTP_403_FORBIDDEN)
            araba.delete()
            return Response({"message": "Araba ilanı silindi."}, status=status.HTTP_204_NO_CONTENT)
        except Araba.DoesNotExist:
            raise NotFound("Bu ilana erişiminiz yok veya ilan bulunamadı.")


class EvAPIView(APIView):
    @jwt_required
    def get(self, request, pk=None):
        """
        Ev bilgilerini getirir. Eğer `pk` verilirse tek bir ev döner.
        """
        if pk:
            try:
                ev = Ev.objects.get(pk=pk)
            except Ev.DoesNotExist:
                raise NotFound("Ev bulunamadı.")
            serializer = EvSerializer(ev)
        else:
            evler = Ev.objects.all()
            serializer = EvSerializer(evler, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @jwt_required
    def post(self, request):
        """
        Yeni bir ev ilanı oluşturur.
        """
        data = request.data
        data["user"] = request.user.id
        serializer = EvSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @jwt_required
    def put(self, request, pk):
        """
        Ev ilanını günceller.
        """
        try:
            ev = Ev.objects.get(pk=pk)
            if ev.user != request.user:  # Kullanıcı yetkilendirme kontrolü
                return Response({"error": "Bu ilanı güncelleme yetkiniz yok."}, status=status.HTTP_403_FORBIDDEN)
        except Ev.DoesNotExist:
            raise NotFound("Bu ilana erişiminiz yok veya ilan bulunamadı.")

        request.data["user"] = request.user.id
        serializer = EvSerializer(ev, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @jwt_required
    def delete(self, request, pk):
        """
        Bir ev ilanını siler.
        """
        try:
            ev = Ev.objects.get(pk=pk)
            if ev.user != request.user:  # Kullanıcı yetkilendirme kontrolü
                return Response({"error": "Bu ilanı silme yetkiniz yok."}, status=status.HTTP_403_FORBIDDEN)
            ev.delete()
            return Response({"message": "Ev ilanı silindi."}, status=status.HTTP_204_NO_CONTENT)
        except Ev.DoesNotExist:
            raise NotFound("Bu ilana erişiminiz yok veya ilan bulunamadı.")
