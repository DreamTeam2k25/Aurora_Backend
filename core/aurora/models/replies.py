from django.db import models
from core.authentication.models import User
from .comments import Comments

class Replies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name='comment')
    reply = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.name
    
    class Meta:
        verbose_name = 'reply'
        verbose_name_plural = 'replies'
        ordering = ['-created_at']
    
    