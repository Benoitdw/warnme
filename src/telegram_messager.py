from src.messager import Messager
from telegram import Bot

class TelegramMessager(Messager):
    """
    Telegram messager class, used to send messages via Telegram.
    """
    def __init__(self) -> None:
        super().__init__()
        self.bot = Bot(token=self.get_envar("TELEGRAM_TOKEN"))
        self.chat_id = self.get_envar("TELEGRAM_CHAT_ID")

    async def send(self, message: str) -> None:
        # Implementation for sending a message via Telegram
        await self.bot.send_message(chat_id=self.chat_id, text=message, )

