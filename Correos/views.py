from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail

def prueba_mail():
	send_mail(
		'Subject herehihhihi',
		'Here is the message.',
		'danielmontecinoszambra@gmail.com',
		['mendrack1@gmail.com',"d.montecinoszambra@uandresbello.edu"],
		fail_silently=False,
	)

# def enviar_multiples_correos(email_destino, tema, cuerpo_mensaje):

import smtplib
import ssl
from django.conf import settings

port = settings.EMAIL_PORT
smtp_server = settings.EMAIL_HOST
sender_email = settings.EMAIL_HOST_USER
password = settings.EMAIL_HOST_PASSWORD
def enviar_emails(asunto, mensaje, correos):
	send_mail(
		asunto,
		mensaje,
		sender_email,
		correos,
		fail_silently=False,
	)
def email():
    # port = settings.EMAIL_PORT
    # smtp_server = settings.EMAIL_HOST
    # sender_email = settings.EMAIL_HOST_USER
    # password = settings.EMAIL_HOST_PASSWORD
    receiver_email = 'mendrack1@gmail.com'
    subject = 'pruebiwis jejijijeiji'
    body = 'Esto fue una prueba enviada desde el codigo con django jejeje'
    message = 'Subject: {}\n\n{}'.format(subject, body)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def enviar_email(email_destino, tema, cuerpo_mensaje):
	receiver_email = email_destino
	subject = tema
	body = cuerpo_mensaje
	message = 'Subject: {}\n\n{}'.format(subject, body)
	context = ssl.create_default_context()

	with smtplib.SMTP(smtp_server, port) as server:
		server.ehlo()  # Can be omitted
		server.starttls(context=context)
		server.ehlo()  # Can be omitted
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)


