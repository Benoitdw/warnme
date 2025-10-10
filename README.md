

## Installation
```bash
pip install git+ssh://git@github.com/Benoitdw/warnme.git
```

## Config
.env file is needed for secrets. It has to be in `$HOME/.config/.warnme`

See the [Wiki](https://github.com/Benoitdw/warnme/wiki) for informations how to create the file.

You can take the .env file as a template.



## Usage
### As CLI
```bash
Usage: warnme [OPTIONS] [MESSAGE]

Options:
  --level [warning|info|fail|success]
                                  Indicate the level of the message
  --help                          Show this message and exit.
```

### As library
```python
from warnme.telegram_messager import TelegramMessager
TelegramMessager().send('hello ! :rocket:') 
```

if you want to make your message mroe Fancy 
```python 
from warnme.telegram_messager import TelegramMessager
from warnme.message import Message, LevelType
TelegramMessager().send(Message('fail', level=LevelType.FAIL) 
```