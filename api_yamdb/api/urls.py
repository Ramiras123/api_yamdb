from django.urls import path, include
from .views import (UserViewSet, CategoryViewSet, 
                    GenreViewSet, TitleViewSet, get_jwt_token, create_user)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register('users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)

auth_urlpatterns = [
    path('token/', get_jwt_token),
    path('signup/', create_user),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth_urlpatterns)),
]