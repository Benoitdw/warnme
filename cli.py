import click
from warnme.telegram_messager import TelegramMessager
from warnme.message import LevelType, Message

@click.command()
@click.argument('message', default='Default message', required=False)
@click.option('--level', help='Indicate the level of the message', type=click.Choice(LevelType, case_sensitive=False), default=LevelType.INFO)
def send_message(message, level):
    TelegramMessager().send(Message(message, level))
    click.echo(f'MESSAGE: {message}')

if __name__ == '__main__':
    send_message()
