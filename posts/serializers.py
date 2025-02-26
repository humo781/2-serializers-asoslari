from django.utils.text import slugify
from rest_framework import serializers
from .models import Post
from catalogs.serializers import CategorySerializer
from tags.serializers import TagSerializer
from authors.serializers import AuthorSerializer

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()
    tags = TagSerializer(many=True)
    authors = AuthorSerializer(read_only=True)
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = ['title', 'content', 'comments_count', 'tags', 'authors', 'categories']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Post tituli kamida 3 ta belgidan iborat bo‘lishi kerak")
        return value

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)


