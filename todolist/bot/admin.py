from django.contrib import admin

from bot.models import TgUser


class BotAdmin(admin.ModelAdmin):
    list_display = ("telegram_user_id", "telegram_chat_id", "user")
    search_fields = ("telegram_user_id", "telegram_chat_id", "user")


admin.site.register(TgUser, BotAdmin)
