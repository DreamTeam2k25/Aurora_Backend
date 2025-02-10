import os
import smtplib

EMAIL_HOST_USER="joaovssouza59@gmail.com"
EMAIL_HOST_PASSWORD="lmbt uiad xsno vedg"


try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        print("Login bem-sucedido!")
except Exception as e:
    print(f"Erro: {e}")