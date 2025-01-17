from django.db import models
from core.authentication.models import User

class Student(models.Model):
    matricula = models.CharField(max_length=255)
    TURMA_CHOICES = [
        ('1info1', '1info1'),
        ('1info2', '1info2'),
        ('1info3', '1info3'),
        ('2info1', '1info1'),
        ('2info2', '1info2'),
        ('2info3', '1info3'),
        ('3info1', '1info1'),
        ('3info2', '1info2'),
        ('3info3', '1info3'),
        ('1agro1', '1agro1'),
        ('1agro2', '1agro2'),
        ('1agro3', '1agro3'),
        ('2agro1', '2agro1'),
        ('2agro2', '2agro2'),
        ('2agro3', '2agro3'),
        ('3agro1', '3agro1'),
        ('3agro2', '3agro2'),
        ('3agro3', '3agro3'),
        ('1quimi', '1quimi'),
        ('2quimi', '2quimi'),
        ('3quimi', '3quimi'),
    ]

    turma = models.CharField(max_length=6, choices=TURMA_CHOICES)
    CURSO_CHOICES = [
        ('informatica', 'Informatica Para Internet'),
        ('quimica', 'Quimica'),
        ('agropecuaria', 'Agropecuaria'),
    ]
    curso = models.CharField(max_length=20, choices=CURSO_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula