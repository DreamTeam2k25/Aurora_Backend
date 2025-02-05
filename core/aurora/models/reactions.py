from django.db import models
from core.authentication.models import User
from .posts import Posts

class Reactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='post')
    reaction = models.BooleanField(default=None, null=True)

    def __str__(self):
        return f'{self.post.title} - {self.reaction}'

