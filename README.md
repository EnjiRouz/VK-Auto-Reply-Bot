# VK-Auto-Reply-Bot

[RU] Бот для ВКонтакте, способный писать сообщения от лица пользователя по заданному расписанию.

[EN] VKontakte User Bot with scheduled message sending.

## Требования (Requirements):
* `pip install vk-api`
* `pip install schedule`
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

## Requirements:
* `pip install vk-api`
* `pip install schedule`
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
