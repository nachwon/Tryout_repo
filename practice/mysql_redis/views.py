from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from mysql_redis.models import Post


class PostListView(ListView):
    model = Post

    def get(self, request, *args, **kwargs):
        context = cache.get('posts')

        if not context:
            posts = Post.objects.all().values('id', 'title', 'content')
            context = {}
            for i in posts:
                context[f'post_{i["id"]}'] = i
            cache.set('posts', context)
        return JsonResponse(context)
