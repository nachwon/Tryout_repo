from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drf_router.serializer import PostSerializer
from mysql_redis.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['post'], detail=True)
    def custom_action(self, request, *args, **kwargs):
        context = {
            'detail': 'this is a custom action',
            'request': f'{request}',
            'args': args,
            'kwargs': kwargs
        }
        return Response(context, status=200)
