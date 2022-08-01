from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    role = models.CharField(default='CREATOR', max_length=30, verbose_name='rôle')
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group = Group.objects.get(name='creators')
        group.user_set.add(self)
