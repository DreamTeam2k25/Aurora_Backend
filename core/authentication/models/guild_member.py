from django.db import models
from core.authentication.models import Student

class Office(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GuildMemberData(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, default=None)
    year_active = models.IntegerField(auto_created=True)
    

    def __str__(self):
        return self.user.name