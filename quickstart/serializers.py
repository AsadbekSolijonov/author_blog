from django.contrib.auth.models import Group, User
from rest_framework import serializers

from quickstart.models import Blog


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    author_id = serializers.SerializerMethodField()
    author_email = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'author', 'author_id', 'author_email', 'title', 'body', 'created_at', 'updated_at')

    def get_author_id(self, obj):
        return obj.author.id

    def get_author(self, obj):
        return obj.author.username

    def get_author_email(self, obj):
        return obj.author.email
