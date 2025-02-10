from django.core.mail import send_mail
from core.authentication.models import Student, User
import os

def send_verification_email(student, url):
    member = student.user
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    GUILD_EMAIL = os.getenv('GUILD_EMAIL')
    API_HOST_URL = os.getenv('API_HOST_URL')
        
    from_email = EMAIL_HOST_USER
    recipient_list = [GUILD_EMAIL]
    verify_link = f'{API_HOST_URL}{url}'

    send_mail(
        subject='Verificação de novo membro', 
        message=f'''
        O estudante {member.name} deseja se tornar um membro no portal Aurora.
        Número de matrícula: {student.matricula}
        Curso: {student.curso}
        Turma: {student.turma}

        Para verificá-lo como membro clique neste link: {verify_link}
        ''',
        from_email=from_email,
        recipient_list=recipient_list
    )