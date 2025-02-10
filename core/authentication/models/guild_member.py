from django.db import models
from core.authentication.models import Student
from datetime import datetime

class Office(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class GuildMemberData(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, default=None)
    year_active = models.IntegerField(null=True, blank=True)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    verified = models.BooleanField(default=False)
    
    def get_year(self, *args, **kwargs):
        if not self.year_active:
            self.year_active = datetime.now().year
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.student.user.name