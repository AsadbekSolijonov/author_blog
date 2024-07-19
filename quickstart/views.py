from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from quickstart.models import Blog
from quickstart.serializers import BlogSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class AuthorBlogsListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to view this

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Blog.objects.filter(author_id=author_id)
