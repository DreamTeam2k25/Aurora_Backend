from django.db import models
from core.authentication.models import User

class Office(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GuildMember(models.Model):
    year_operation = models.IntegerField()
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email