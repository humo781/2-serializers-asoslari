from django.utils.text import slugify
from rest_framework import serializers
from .models import Post
from authors.serializers import AuthorSerializer

class PostSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True)
    comments_count = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    def get_category(self, obj):
        from catalogs.serializers import CategorySerializer
        category = CategorySerializer(obj.categories).data
        return category

    def get_tags(self, obj):
        from tags.serializers import TagSerializer
        tags = TagSerializer(obj.tags.all(), many=True).data
        return tags

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = ['title', 'content', 'comments_count', 'authors', 'category', 'tags']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Post tituli kamida 3 ta belgidan iborat bo‘lishi kerak")
        return value

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)


