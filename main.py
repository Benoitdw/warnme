from src.telegram_messager import TelegramMessager
import asyncio


if __name__ == "__main__":
    # Create an instance of TelegramMessager
    messager = TelegramMessager()
    
    # Send a test message
    asyncio.run(messager.send("Hello, this is a test message from warnMe!"))
    