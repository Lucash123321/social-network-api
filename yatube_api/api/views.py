from rest_framework import viewsets
from posts.models import Post
from api.serializer import (
    PostSerializer
)


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


