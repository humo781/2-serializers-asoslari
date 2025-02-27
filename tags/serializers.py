from django.utils.text import slugify
from rest_framework import serializers
from .models import Tag
from posts.serializers import PostSerializer


class TagPostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['name', 'posts']

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)

class TagSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['name', 'post_count']

    def get_post_count(self, obj):
        return obj.posts.count()
