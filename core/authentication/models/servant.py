from django.db import models
from core.authentication.models import User

class Student(models.Model):
    setor = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    validate = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.name