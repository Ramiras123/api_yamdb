from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters, status, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from .permissions import (IsAdminModeratorAuthorOrReadOnly,
                          IsAdminOrSuperuserOrReadOnly,
                          IsAdmin)
from .serializers import UserSerializers, UserEditSerializer, TokenSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    #permission_classes =
    filter_backends = (filters.SearchFilter,)
    filters_fields = ('username',)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(methods=['get', 'patch'],
            detail=False,
            serializer_class=UserEditSerializer,
            url_path='me')
    def user_self_profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(
            user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User,
                             username=serializer.validated_data['username'])
    if default_token_generator.check_token(
        user, serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
