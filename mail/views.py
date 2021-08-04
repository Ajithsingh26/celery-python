from django.shortcuts import render
from django.http import HttpResponse
from .tasks import  send_email


def send_mail_func(request):
    send_email.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')

