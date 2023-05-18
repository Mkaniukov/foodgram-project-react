from django.contrib.auth import get_user_model
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.pagination import LimitPageNumberPagination, LimitPageFollowNumberPagination
from .models import Follow
from .serializers import FollowSerializer, ShowFollowSerializer

User = get_user_model()


class CustomUserViewSet(DjoserUserViewSet):
    pagination_class = LimitPageNumberPagination

    @action(methods=['get'], detail=False,
            permission_classes=[IsAuthenticated])
    def subscriptions(self, request):
        user = self.request.user
        users = User.objects.filter(following__user=user)
        paginator = LimitPageFollowNumberPagination()
        paginator.page_size_query_param = 'recipes_limit'
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = ShowFollowSerializer(
            paginated_users, many=True, context={'request': request}
        )
        return paginator.get_paginated_response(serializer.data)

    @action(methods=['post', 'delete'], detail=True,
            permission_classes=[IsAuthenticated], )
    def subscribe(self, request, id):
        user = self.request.user
        author = get_object_or_404(User, id=id)
        serializer = FollowSerializer(data={'user': user.id, 'author': id})
        if request.method == 'POST':
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            serializer = ShowFollowSerializer(author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        obj = get_object_or_404(Follow, user=user, author__id=id)
        obj.delete()
        return Response('Подписка удалена', status=status.HTTP_204_NO_CONTENT)
