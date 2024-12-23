from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Register API
class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        password_confirm = request.data.get('password_confirm')

        if password != password_confirm:
            return Response({"error": "Şifreler eşleşmiyor."}, status=400)
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Bu kullanıcı adı zaten alınmış."}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "Kayıt başarılı!"}, status=201)


# Login API
class LoginAPIView(APIView):
    """
    Kullanıcı giriş yaparken token döndüren endpoint.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            token = RefreshToken.for_user(user)
            return Response({
                "access": str(token.access_token),
                "refresh": str(token)
            }, status=200)
        
        return Response({"error": "Kullanıcı adı veya şifre hatalı."}, status=401)


# Repassword API
class RepasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        new_password_confirm = request.data.get('new_password_confirm')

        if not request.user.check_password(old_password):
            return Response({"error": "Eski şifre hatalı."}, status=400)
        
        if new_password != new_password_confirm:
            return Response({"error": "Yeni şifreler eşleşmiyor."}, status=400)

        request.user.set_password(new_password)
        request.user.save()
        return Response({"message": "Şifre başarıyla güncellendi."}, status=200)


# Logout API
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Token'i geçersiz kılar
            return Response({"message": "Çıkış işlemi başarılı."}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
