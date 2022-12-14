from threading import Thread
from flask import render_template, current_app
from flask_mail import Message
from flask_babel import _
from app import mail
from app.models import User

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(subject:str, sender:str, recipients:list[str], text_body:str, html_body:str):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app, msg)).start()

def send_password_reset_email(user: User):
    token = user.get_reset_password_token()
    send_mail(_('[Microblog]Reset Password'), 
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
        html_body=render_template('email/reset_password.html',
                                         user=user, token=token))