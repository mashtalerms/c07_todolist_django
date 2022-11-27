from django.db import models

from core.models import User


class TgUser(models.Model):

    telegram_chat_id = models.IntegerField()
    telegram_user_ud = models.IntegerField()
    local_user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
