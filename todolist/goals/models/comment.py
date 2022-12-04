from django.db import models

from core.models import User
from goals.models.base import DatesModelMixin
from goals.models.goal import Goal


class Comment(DatesModelMixin):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    text = models.CharField(verbose_name="Текст", max_length=225)
    goal = models.ForeignKey(Goal, verbose_name="Цель", on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
