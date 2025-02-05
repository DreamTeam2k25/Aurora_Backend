from django.db import models
from core.authentication.models import User
from core.aurora.models import Posts

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='post')
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta: 
        verbose_name = 'Comment'
        verbose_name_plural = "Comments"
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.name} - {self.post.title}'

    