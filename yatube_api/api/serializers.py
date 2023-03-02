from rest_framework import serializers
from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'group', 'pub_date', 'text', 'image')
        read_only_fields = ('id', 'author', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('post', 'author', 'text', 'created')
        read_only_fields = ('author', 'post')