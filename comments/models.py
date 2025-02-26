from django.db import models
from posts.models import Post

class Comment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

    def __str__(self):
        return f"{self.author_name}'s Comment"
