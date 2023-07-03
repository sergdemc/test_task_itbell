from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.serializer import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Post.objects.filter(pk=pk)
        return Post.objects.all()
