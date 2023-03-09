from rest_framework import serializers
from .models import Post, Comment, Follow, Group


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


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ('user', 'author')
        read_only_fields = ('user', )

    def validate(self, attrs):
        already_follow = Follow.objects.filter(author=attrs['author'])
        if self.context['request'].user == attrs['author'] or already_follow:
            raise serializers.ValidationError
        return attrs


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')
