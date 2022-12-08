from threading import Thread
from flask import render_template
from flask_mail import Message
from flask_babel import _
from app import mail, myapp

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(subject:str, sender:str, recipients:list[str], text_body:str, html_body:str):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(myapp, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail(_('[Microblog]Reset Password'), 
        sender=myapp.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
        html_body=render_template('email/reset_password.html',
                                         user=user, token=token))