from django.db import models
from rest_framework.exceptions import ValidationError


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def clean(self):
        if len(self.name) < 5:
            raise ValidationError({"name": "To‘liq ismingizni kiriting!"})

    def __str__(self):
        return self.name
