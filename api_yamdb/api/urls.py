from django.urls import path, include
from api.views import UserViewSet, get_jwt_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('users', UserViewSet, basename='users')

auth_urlpatterns = [
    path('token/', get_jwt_token)
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth_urlpatterns)),
]