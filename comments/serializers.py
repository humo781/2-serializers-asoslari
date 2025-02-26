import re
from rest_framework import serializers
from .models import Comment

class RecursiveCommentSerializer(serializers.Serializer):
    def to_representation(self, value):
        return CommentSerializer(value).data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['posts', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'replies']

    def validate_parent_comment(self, comment):
        if comment:
            level = 1
            while comment.parent_comment:
                comment = comment.parent_comment
                level += 1

            if level >= 3:
                raise serializers.ValidationError("Siz 3-darajadan chuqurroq izoh qoldira olmaysiz.")
        return comment

    def validate_email(self, author_email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, author_email):
            raise serializers.ValidationError("Noto‘g‘ri email formati! To‘g‘ri format: example@example.com")
        return author_email
