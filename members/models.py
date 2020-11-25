from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class Team(models.Model):
    ceo = models.CharField(max_length=32)
    name = models.CharField(max_length=32, unique=True, blank=False, null=False)
    about = models.CharField(max_length=400)
    avatar = models.ImageField(upload_to='uploads/teams/avatars/')
    is_verified = models.BooleanField(default=False)

    # - Team socials
    twitter = models.CharField(max_length=20)
    instagram = models.CharField(max_length=20)
    location = models.CharField(max_length=74)

    def __str__(self):
        return f'{self.name} | Based in {self.location} | Owned by {self.ceo}'


class Member(AbstractUser):
    is_verified = models.BooleanField(default=False)
    current_team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)


class Connection(models.Model):
    connector = models.ForeignKey(Member, related_name='connector', on_delete=models.CASCADE)
    connectee = models.ForeignKey(Member, related_name='connectee', on_delete=models.CASCADE)
    is_connected = models.BooleanField(default=False)

    def __str__(self):
        return f'Connection between dick and cock' # Looking for a VC daddy! (Venture capital)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)