from celery import shared_task
from config.celery import app
from django.core.mail import send_mail
from core.authentication.models import Student
import os

@shared_task
def add(x, y):
    value = x + y
    print(f"Task executada: {value}")
    return value

@app.task(queue="emails")
def send_verification_email_task(student_id, url):
    student = Student.objects.get(id=student_id)
    member = student.user
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    GUILD_EMAIL = os.getenv('GUILD_EMAIL')
    API_HOST_URL = os.getenv('API_HOST_URL')

    from_email = EMAIL_HOST_USER
    recipient_list = [GUILD_EMAIL]
    verify_link = f'{API_HOST_URL}{url}'

    send_mail(
        subject='Verificação de novo membro',
        message='Olá, este é um e-mail de verificação. Caso não consiga visualizar, favor abrir em um navegador.',
        html_message=f'''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Email de Verificação</title>
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    font-family: Arial, sans-serif;
                    background-color: #ffffff;
                }}

                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}

                .header {{
                    background-color: #007BFF;
                    padding: 20px;
                    text-align: center;
                    color: white;
                }}

                .content {{
                    padding: 20px;
                    background-color: #f4f4f4;
                    border-radius: 8px;
                }}

                .content h1 {{
                    color: #333;
                }}

                .content p {{
                    color: #555;
                    font-size: 16px;
                }}

                .button {{
                    display: inline-block;
                    padding: 15px 25px;
                    background-color: #007BFF;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-size: 18px;
                    margin-top: 20px;
                }}

                .footer {{
                    text-align: center;
                    padding: 10px;
                    background-color: #007BFF;
                    color: white;
                    font-size: 12px;
                }}

                @media only screen and (max-width: 600px) {{
                    .container {{
                        width: 100%;
                        padding: 10px;
                    }}

                    .button {{
                        padding: 12px 20px;
                        font-size: 16px;
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Verificação de novo membro</h1>
                </div>
                <div class="content">
                    <h1>O estudante {member.name} deseja se tornar um membro no portal Aurora.</h1>
                    <p> Número de matrícula: {student.matricula} </p>
                    <p>Curso: {student.curso}</p>
                    <p>Turma: {student.turma}</p>
                    <p>Para verificá-lo como membro, clique neste botão:</p>
                    <a href="{verify_link}" class="button">Verificar membro</a>
                    <p>Se ele não for membro, ignore este e-mail.</p>
                </div>
                <div class="footer">
                    <p>&copy; 2025 Aurora. Todos os direitos reservados.</p>
                </div>
            </div>
        </body>
        </html>
        ''',
        from_email=from_email,
        recipient_list=recipient_list
    )

@app.task(queue="emails")
def send_email_task(email):
    print(f"Enviando e-mail para {email}")
    return True