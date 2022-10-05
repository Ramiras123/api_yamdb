from django.urls import path, include
from .views import UserViewSet, get_jwt_token, create_user
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register('users', UserViewSet, basename='users')

auth_urlpatterns = [
    path('token/', get_jwt_token),
    path('signup/', create_user),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth_urlpatterns)),
]