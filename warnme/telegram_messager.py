from warnme.messager import Messager
from telegram import Bot
from warnme.message import Message,level_emoji_map

class TelegramMessager(Messager):
    """
    Telegram messager class, used to send messages via Telegram.
    """
    def __init__(self) -> None:
        super().__init__()
        self.bot = Bot(token=self.get_envar("TELEGRAM_TOKEN"))
        self.chat_id = self.get_envar("TELEGRAM_CHAT_ID")

    async def _send(self, message: str) -> None:
        # Implementation for sending a message via Telegram
        await self.bot.send_message(chat_id=self.chat_id, text=message )

    def format_message(self, message:Message | str ) -> str:
        if isinstance(message, str):
            return message 
        return f"{level_emoji_map.get(message.level, message.level)} {message.text}" 

