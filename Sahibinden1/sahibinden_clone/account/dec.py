from functools import wraps
from datetime import datetime, timedelta, timezone
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()  # Özel bir User modeli varsa onu kullanır

def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthenticationFailed('Token gereklidir.')

        try:
            # Token'ı "Bearer <token>" formatında aldığımız için sadece token'ı alıyoruz
            if not token.startswith("Bearer "):
                raise AuthenticationFailed('Token formatı hatalı. "Bearer <token>" olmalı.')

            token = token.split(' ')[1]

            # Token'ı decode ediyoruz
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.SIMPLE_JWT.get("ALGORITHM")])
            user_id = payload.get('user_id')

            if not user_id:
                raise AuthenticationFailed('Token içerisinde id bilgisi bulunamadı.')

            user = User.objects.get(id=user_id)  # Token'dan alınan user_id ile kullanıcıyı buluyoruz
            request.user = user  # Kullanıcıyı request'e bağlıyoruz

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token süresi dolmuş.')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Geçersiz token.')
        except User.DoesNotExist:
            raise AuthenticationFailed('Kullanıcı bulunamadı.')

        return view_func(self, request, *args, **kwargs)

    return _wrapped_view


def create_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        'iat': datetime.now(timezone.utc),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token
