from src.telegram_messager import TelegramMessager

if __name__ == "__main__":
    # Create an instance of TelegramMessager
    messager = TelegramMessager()
    
    # Send a test message
    messager.send("Hello, this is a test message from warnMe!")
    
    print("Message sent successfully!")