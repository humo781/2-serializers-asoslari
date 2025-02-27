from django.utils.text import slugify
from rest_framework import serializers
from .models import Category
from posts.serializers import PostSerializer


class CategoryPostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'description', 'posts']

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)

class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'description', 'post_count', 'posts']

    def get_post_count(self, obj):
        return obj.posts.count()
