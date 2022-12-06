from flask import render_template
from flask_mail import Message
from app import mail

def send_mail(subject:str, sender:str, recipients:list[str], text_body:str, html_body:str):
    msg = Message(subject, sender, recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail('[Microblog]Reset Password', 
        sender='eric',
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
        html_body=render_template('email/reset_password.html',
                                         user=user, token=token))