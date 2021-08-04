from celery import shared_task
from django.core.mail import send_mail
from time import sleep
from django.conf import settings

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task(bind=True)
def send_email(self):
    message = "hi,Its works"
    to_email = 'ajithsingh.doodleblue@gmail.com'
    send_mail(
        subject = "Hi! Celery Testing",
        message=message, 
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False,
        )
    return "Done"