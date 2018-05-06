from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mysql_redis.models import Post


class PostSerializer(serializers.ModelSerializer):
    BAD_WORDS = [
        'shit',
        'fuck'
    ]

    class Meta:
        model = Post
        fields = ('id', 'title', 'content')

    def validate(self, data):
        too_short_title = len(data['title']) < 10
        too_short_content = len(data['content']) < 10

        if too_short_title or too_short_content:
            raise ValidationError('Either title or content is too short!')
        return data

    def validate_title(self, data) -> str:
        for word in self.BAD_WORDS:
            if word in data.lower():
                raise ValidationError(f"title contains an inappropriate word: '{word}'")
        return data

    def validate_content(self, data) -> str:
        for word in self.BAD_WORDS:
            if word in data.lower():
                raise ValidationError(f"content contains an inappropriate word: '{word}'")
        return data
