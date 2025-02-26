from django.utils.text import slugify
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    category_post_count = serializers.SerializerMethodField()
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def get_category_post_count(self, obj):
        return obj.posts.count()

    class Meta:
        model = Category
        fields = ['name', 'description', 'category_post_count', 'posts']

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)
