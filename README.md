# VK Auto Reply Bot

[RU] Бот для ВКонтакте, способный писать сообщения от лица пользователя по заданному расписанию, с использованием технологий NLU (Nature Language Understanding) или отвечая на строго заданные сообщения.

YouTube-гайд по проекту: https://youtu.be/FPJ5bgYLOzQ

[EN] VKontakte User Bot with scheduled message sending, NLU (Nature Language Understanding) and managed responses

YouTube Guide for this project: https://youtu.be/FPJ5bgYLOzQ

## Требования:
* `pip install -r requirements.txt`
* создать `.env`-файл для того, чтобы хранить переменные окружения `ACCESS_TOKEN` и `USER_ID`

## Пример .env-файла:
```
ACCESS_TOKEN="1q2w3e4r5t6y7u8i9o..."
USER_ID="1234567890"
```

## Где взять ACCESS_TOKEN?
* быстрый путь: использовать https://vkhost.github.io/
* сложный путь: декомпилировать приложение KateMobile и получить данные приложения для получения токена через запрос
* стандартный путь: создать своё приложение для ВКонтакте [см. документацию](https://vk.com/dev/manuals)

## Примеры использования
##### Использование Bot:
```python
from simple_bot import Bot

# создание и запуск обычного бота
bot = Bot()
    
# отправка тестового сообщения
bot.send_message()
    
# отправка сообщения с заданными параметрами
bot.send_message(receiver_user_id="1234567890", message_text="Привет, это сообщение отправлено автоматически")
```

##### Использование Scheduled Bot:
```python
from scheduled_bot import ScheduledBot

# создание и запуск бота, отправляющего сообщения по расписанию
scheduled_bot = ScheduledBot()
```

##### Использование LongPoll Bot:
```python
from longpoll_bot import LongPollBot

# создание и запуск бота, автоматически отвечающего на заданные сообщения
long_poll_bot = LongPollBot()
long_poll_bot.run_long_poll()
```

##### Использование NLU LongPoll Bot:
```python
from nlu_longpoll_bot import NLULongPollBot

# создание и запуск бота, автоматически отвечающего на любые сообщения
nlu_longpoll_bot = NLULongPollBot()
nlu_longpoll_bot.run_long_poll()
```

## Requirements:
* `pip install requirements.txt`
* create `.env` file to store `ACCESS_TOKEN` and `USER_ID` values

## .env-file example:
```
ACCESS_TOKEN="1q2w3e4r5t6y7u8i9o..."
USER_ID="1234567890"
```

## How to get ACCESS_TOKEN?
* fast way: to use https://vkhost.github.io/
* advanced way: decompile KateMobile app and get its data to make auth request
* normal way: create your own app using [docs](https://vk.com/dev/manuals)

## Usage Examples
##### Simple Bot Usage:
```python
from simple_bot import Bot

# simple bot start
bot = Bot()
    
# sending test message
bot.send_message()
    
# sending message with initialized properties
bot.send_message(receiver_user_id="1234567890", message_text="Hello, this message was sent automatically")
```

##### Scheduled Bot Usage:
```python
from scheduled_bot import ScheduledBot

# scheduled bot start
scheduled_bot = ScheduledBot()
```

##### LongPoll Bot Usage:
```python
from longpoll_bot import LongPollBot

# long poll bot start with an automatic response to managed messages
long_poll_bot = LongPollBot()
long_poll_bot.run_long_poll()
```

##### NLU LongPoll Bot Usage:
```python
from nlu_longpoll_bot import NLULongPollBot

# nature language understanding long poll bot start with an automatic response to user messages
# russian corpus used
nlu_longpoll_bot = NLULongPollBot()
nlu_longpoll_bot.run_long_poll()
```
