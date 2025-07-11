

## Config
.env file is needed for secrets. It has to be in `$HOME/.config/.warnme`


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