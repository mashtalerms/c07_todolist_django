from django.urls import path

from bot.views import TgUserUpdateView

urlpatterns = [
    path("verify", TgUserUpdateView.as_view()),
]
