import random
from django.core.management import BaseCommand

from bot.models import TgUser
from bot.tg.bot.tg.client import TgClient
from bot.tg.bot.tg.dc import GetUpdatesResponse
from c07_todolist.settings import BOT_TOKEN
from goals.models.category import Category
from goals.models.goal import Goal
from goals.models.participant import BoardParticipant


class Command(BaseCommand):
    help = 'Logic of telegram bot'

    def __init__(self):
        self.offset = 0
        self.tg_client = TgClient(BOT_TOKEN)
        self.response: GetUpdatesResponse

        self.user: TgUser = None
        self.tg_user: TgUser
        self.chat_id: int
        self.tg_user_id: int
        self.message: str
        self.message_id: int = 0
        self.reply_required: bool = False

        self.category: Category
        self.goal: Goal
        self.category_mode: bool = False
        self.goal_mode: bool = False

        super().__init__()

    def handle(self, *args, **options):
        while True:
            self._get_response()

            if self.reply_required:
                if self.user:
                    reply = self._main_logic()
                else:
                    reply = self._verify()

                self._send_reply(reply=reply)
                self.reply_required = False

    def _get_response(self) -> None:
        """Get data from response"""
        self.response = self.tg_client.get_updates(offset=self.offset)

        for item in self.response.result:
            self.chat_id = item.message.chat.id
            self.tg_user_id = item.message.from_.id
            self.message = item.message.text
            self.offset = item.update_id + 1

            self.user = TgUser.objects.filter(
                tg_user_id=self.tg_user_id, user_id__isnull=False
            ).first()

            # check if message is new
            if not self.message_id == item.message.message_id:
                self.reply_required = True

            self.message_id = item.message.message_id

    def _main_logic(self) -> str:
        """Logic for verified user"""

        if self.message == '/cancel':
            self.category_mode = False
            self.goal_mode = False
            reply = f'Операция прервана, введите команду'
        elif self.category_mode:
            reply = self._choose_category()
        elif self.goal_mode:
            reply = self._create_goal()

        # key commands
        elif self.message == '/goals':
            reply = self._goals()
        elif self.message == '/create':
            reply = self._create()

        else:
            reply = 'Неизвестная команда'

        return reply

    def _verify(self) -> str:
        """Verifying user"""
        verification_code = random.randint(10000, 99999)

        self.tg_user = TgUser.objects.filter(tg_user_id=self.tg_user_id).first()
        if not self.tg_user:
            TgUser.objects.create(
                tg_user_id=self.tg_user_id,
                tg_chat_id=self.chat_id,
                verification_code=verification_code
            )
        else:
            self.tg_user.verification_code = verification_code
            self.tg_user.save()

        reply = (f"Аккаунт не подтвержден. "
                 f"Для подтверждения необходимо ввести код: {verification_code} "
                 f"на в личном кабинете на сайте.")
        return reply

    def _goals(self) -> list:
        """Logic for /goals command - choose category"""
        goals = Goal.objects.filter(
            category__board__participants__user=self.user.user, is_deleted=False
        ).only('id', 'title')
        prefix = ['Cписок ваших целей:']
        reply = [f'#{goal.id} {goal.title}' for goal in goals]
        return prefix + reply

    def _create(self) -> list:
        """Logic for /create command - list of categories"""
        categories = Category.objects.filter(
            board__participants__user=self.user.user,
            board__participants__role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
            is_deleted=False
        ).only('id', 'title')
        self.category_mode = True
        prefix = ['Введите номер категории зи списка доступных:']
        reply = [f'#{category.id} {category.title}' for category in categories]
        return prefix + reply

    def _choose_category(self) -> str:
        """Logic for /create command - choose category"""

        if not self.message.isnumeric():
            return f'Выбрана неверная категория'

        self.category = Category.objects.filter(
            pk=self.message,
            board__participants__user=self.user.user,
            board__participants__role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
            is_deleted=False
        ).first()

        if not self.category:
            reply = f'Выбрана неверная категория'
        else:
            reply = (f'Выбрана категория {self.category.title}. '
                     f'Введите цель')
            self.goal_mode = True
            self.category_mode = False

        return reply

    def _create_goal(self) -> str:
        """Logic for /create command - create goal"""
        self.goal = Goal.objects.create(
            user=self.user.user, title=self.message, category=self.category
        )
        self.goal_mode = False
        return f'Цель "{self.goal.title}" создана'

    def _send_reply(self, reply: str | list) -> None:
        """Send reply"""
        if isinstance(reply, list):
            for item in reply:
                self.tg_client.send_message(chat_id=self.chat_id, text=item)
        else:
            self.tg_client.send_message(chat_id=self.chat_id, text=reply)
