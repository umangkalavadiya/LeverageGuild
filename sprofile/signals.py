from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from sprofile.models import Sprofile


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Sprofile(user=instance)
        profile.save()
