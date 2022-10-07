from django.urls import path, include
from .views import (UserViewSet, CategoryViewSet,
                    GenreViewSet, TitleViewSet,
                    ReviewViewSet, CommentViewSet,
                    get_jwt_token, create_user)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router.register('titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

auth_urlpatterns = [
    path('token/', get_jwt_token),
    path('signup/', create_user),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth_urlpatterns)),
]
