from rest_framework import serializers
from posts.models import Post
from users.serializer import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created_at', 'author')
