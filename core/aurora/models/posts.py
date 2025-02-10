from django.db import models
from core.authentication.models import User
from core.uploader.models import Image

class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]


class PostImage(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="images")
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post Image"
        verbose_name_plural = "Post Images"
        ordering = ["id"]