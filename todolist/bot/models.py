from django.db import models

from core.models import User


class TgUser(models.Model):

    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграм"

    tg_user_id = models.IntegerField(verbose_name="ID пользователя в телеграм", null=True)
    tg_chat_id = models.IntegerField(verbose_name="ID чата в телеграм", null=True)
    verification_code = models.IntegerField(verbose_name="Код для верефикации")
    user = models.ForeignKey(
        User, verbose_name="Пользователь телеграм", on_delete=models.PROTECT, null=True, blank=True)
