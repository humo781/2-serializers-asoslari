import re
from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

    def validate_email(self, value):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, value):
            raise serializers.ValidationError("Noto‘g‘ri email formati! To‘g‘ri format: example@example.com")
        return value

    def validate_name(self, name):
        if len(name) < 5:
            raise serializers.ValidationError("to'liq ismingizni kiriting")
        return name
