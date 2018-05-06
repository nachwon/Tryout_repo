from django.core.cache import cache
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        cache.delete('posts')
        print('saved')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.delete('posts')
        super().delete(*args, **kwargs)
