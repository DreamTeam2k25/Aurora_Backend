from django.db import models
from core.authentication.models import User

class Ombdusman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    description = models.TextField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email} - {self.description}'