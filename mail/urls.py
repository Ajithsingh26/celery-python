from django.urls import path
from mail import views

urlpatterns = [
    path('sendmail/',views.send_mail_func,name="index")
]