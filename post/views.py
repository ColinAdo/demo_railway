from rest_framework import viewsets, permissions

from .models import Post
from .serializers import PostSerializer

class PostViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
