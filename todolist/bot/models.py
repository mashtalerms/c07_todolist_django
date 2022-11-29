from django.db import models

from core.models import User


class TgUser(models.Model):

    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграм"

    telegram_chat_id = models.IntegerField(verbose_name="ID чата телеграм")
    telegram_user_id = models.IntegerField(verbose_name="ID пользователя телеграм")
    verification_code = models.IntegerField(verbose_name="Код для верефикации")
    user = models.ForeignKey(
        User, verbose_name="Пользователь телеграм", on_delete=models.PROTECT, null=True, blank=True)
