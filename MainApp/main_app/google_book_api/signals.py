from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Library


@receiver(post_save, sender=User)
def create_library(sender, instance, created, **kwargs):
    if created:
        a = Library.objects.create(owner=instance)
        a.save()
