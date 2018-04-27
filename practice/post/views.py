from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from post.models import Post


class PostListView(ListView):
    model = Post

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().values('id', 'title', 'content')
        context = {}
        for i in posts:
            context[f'post_{i["id"]}'] = i
        return JsonResponse(context)
