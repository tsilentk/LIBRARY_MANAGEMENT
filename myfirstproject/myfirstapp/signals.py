from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import Settings



# def createProfile(sender,instance,created,**kwargs):
#     if created:
#         user=instance
#         profile=Profile.objects.create(
#             user=user,
#             username=user.username,
#             email=user.email,
#             name=user.firstname,
#         )
#         subject='welcome'
#         message='we are glad'

#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,
#             [profile.email],
#             fail_silently=False
#         )
