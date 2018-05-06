from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from drf_router.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, base_name='posts')

urlpatterns = [
    url(r'', include(router.urls))
]
