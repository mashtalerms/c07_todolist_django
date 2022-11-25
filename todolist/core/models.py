from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        ordering = ['username']

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.email

