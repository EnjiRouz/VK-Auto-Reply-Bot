# Документация: https://github.com/python273/vk_api
# Получить токен: https://vkhost.github.io/
# TODO прикрутить корпус для чат-бота и закинуть в longpool для автоматизации ответов на частые вопросы

import vk_api  # использование VK API
from vk_api.utils import get_random_id  # снижение количества повторных отправок сообщения
from dotenv import load_dotenv  # загрузка информации из .env-файла
import os  # работа с файловой системой
import random  # генератор случайных чисел
import schedule  # выполнение отложенных задач

# прозвища, участвующие в генерации фраз
pet_names = [
    "котёнок",
    "зайчонок",
    "малыш",
    "кингурёнок",
    "солнышко",
    "котик",
    "чертёнок",
    "мышонок",
    "хомячок",
    "пёсик",
    "пупсик",
    "золотце",
    "милый",
    "медвежонок",
    "членастик",
    "писюн",
    "бяка"
]


def wish_good_morning():
    """
    Отправка случайного пожелания доброго утра
    """
    pet_name = pet_names[random.randint(0, len(pet_names) - 1)]
    phrases = [
        "Доброе утро, {}! Как спалось?".format(pet_name),
        "Утро, {}! Какой план у тебя на день?".format(pet_name),
        "утро, {}".format(pet_name),
        "доброе утро, {}, какой сон тебе снился сегодня?".format(pet_name),
        "утро, уже позавтракал?".format(pet_name)
    ]
    message = phrases[random.randint(0, len(phrases) - 1)]
    send_message(vk_api_access=vk, receiver_user_id=user_id, message_text=message)


def talk_about_lunch():
    """
    Отправка случайного сообщения про обед
    """
    pet_name = pet_names[random.randint(0, len(pet_names) - 1)]
    phrases = [
        "угадай, чем я сегодня обедала, {}".format(pet_name),
        "приятного аппетита, {}!".format(pet_name),
        "а что ты любишь кушать, {}?".format(pet_name),
        "Что ты ел сегодня, {}?".format(pet_name),
    ]
    message = phrases[random.randint(0, len(phrases) - 1)]
    send_message(vk_api_access=vk, receiver_user_id=user_id, message_text=message)


def ask_how_the_day_was():
    """
    Отправка случайного вопроса про сегодняшние дела
    """
    pet_name = pet_names[random.randint(0, len(pet_names) - 1)]
    phrases = [
        "как твой день проходит, {}?".format(pet_name),
        "чем занимался сегодня, {}?".format(pet_name),
        "Признавайся, что делал весь день, {}?".format(pet_name),
        "чего успел натворить за сегодня, {}?".format(pet_name)
    ]
    message = phrases[random.randint(0, len(phrases) - 1)]
    send_message(vk_api_access=vk, receiver_user_id=user_id, message_text=message)


def wish_good_night():
    """
    Отправка случайного пожелания на ночь
    """
    pet_name = pet_names[random.randint(0, len(pet_names) - 1)]
    phrases = [
        "Доброй ночи, {}!".format(pet_name),
        "Сладких снов, {})".format(pet_name),
        "спи крепко, {}".format(pet_name),
        "спокнойно ночи тебе, {}, завтра продолжим".format(pet_name)
    ]
    message = phrases[random.randint(0, len(phrases) - 1)]
    send_message(vk_api_access=vk, receiver_user_id=user_id, message_text=message)


def do_auth():
    """
    Авторизация за пользователя (не за группу или приложение)
    Использует переменную, хранящуюся в файле настроек окружения .env в виде строки ACCESS_TOKEN="1q2w3e4r5t6y7u8i9o..."
    :return: возможность работать с API
    """
    token = os.getenv("ACCESS_TOKEN")
    vk_session = vk_api.VkApi(token=token)
    return vk_session.get_api()


def create_schedule():
    """
    Создание расписания отправки сообщений со случайным временем в заданном промежутке
    """

    morning_time = "0"+str(random.randint(7, 9))+":"+str(random.randint(10, 59))
    lunch_time = str(random.randint(11, 13))+":"+str(random.randint(10, 59))
    miss_time = str(random.randint(15, 17))+":"+str(random.randint(10, 59))
    evening_time = str(random.randint(18, 20))+":"+str(random.randint(10, 59))
    night_time = str(random.randint(22, 23))+":"+str(random.randint(10, 59))

    schedule.every().day.at(morning_time).do(wish_good_morning)
    schedule.every().day.at(lunch_time).do(talk_about_lunch)
    schedule.every().day.at(evening_time).do(ask_how_the_day_was)
    schedule.every().day.at(night_time).do(wish_good_night)
    schedule.every().day.at("00:00").do(restart_schedule)

    print("Schedule:" + "\n" +
          morning_time + "\n" +
          lunch_time + "\n" +
          miss_time + "\n" +
          evening_time + "\n" +
          night_time)


def restart_schedule():
    """
    Перезапуск расписания для обновления случайного времени отправки сообщений
    """
    schedule.clear()
    create_schedule()


def send_message(vk_api_access, receiver_user_id:str, message_text:str):
    """
    Отправка сообщения
    :param vk_api_access: доступ к VK API после авторизации
    :param receiver_user_id: уникальный идентификатор получателя сообщения
    :param message_text: текст отправляемого сообщения
    """
    try:
        vk_api_access.messages.send(user_id=receiver_user_id, message=message_text, random_id=get_random_id())
        print("Message Sent: "+message_text)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    # загрузка информации из .env-файла
    load_dotenv()

    # получение id пользователя из файла настроек окружения .env в виде строки USER_ID="1234567890"
    user_id = os.getenv("USER_ID")
    print(user_id)

    # авторизация
    vk = do_auth()

    # создание расписания отправки сообщений
    create_schedule()

    # отправка сообщения заданному пользователю по расписанию
    while True:
        schedule.run_pending()
