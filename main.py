# Документация: https://github.com/python273/vk_api
# Получить токен: https://vkhost.github.io/
# TODO прикрутить корпус для чат-бота и закинуть в longpool для автоматизации ответов на частые вопросы

import vk_api  # использование VK API
from vk_api.utils import get_random_id  # снижение количества повторных отправок сообщения
from dotenv import load_dotenv  # загрузка информации из .env-файла
import os  # работа с файловой системой
import random  # генератор случайных чисел
import schedule  # выполнение отложенных задач
import time  # работа с датой и временем (используется только для логов)


class Bot:
    """
    Базовый класс бота ВКонтакте
    """

    # доступ к API ВКонтакте
    vk_api_access = None

    # пометка авторизованности
    authorized = False

    # id пользователя ВКонтакте (например, 1234567890) в виде строки
    # можно использовать, если диалог будет вестись только с конкретным человеком
    default_user_id = None

    def __init__(self):
        """
        Инициализация бота при помощи получения доступа к API ВКонтакте
        """
        # загрузка информации из .env-файла
        load_dotenv()

        # авторизация
        self.vk_api_access = self.do_auth()

        if self.vk_api_access is not None:
            self.authorized = True

        # получение id пользователя из файла настроек окружения .env в виде строки USER_ID="1234567890"
        self.default_user_id = os.getenv("USER_ID")

    def do_auth(self):
        """
        Авторизация за пользователя (не за группу или приложение)
        Использует переменную, хранящуюся в файле настроек окружения .env в виде строки ACCESS_TOKEN="1q2w3e4r5t6y7u8i9o..."
        :return: возможность работать с API
        """
        token = os.getenv("ACCESS_TOKEN")
        try:
            vk_session = vk_api.VkApi(token=token)
            return vk_session.get_api()
        except Exception as error:
            print(error)
            return None

    def send_message(self, receiver_user_id: str = None, message_text: str = "тестовое сообщение"):
        """
        Отправка сообщения от лица авторизованного пользователя
        :param receiver_user_id: уникальный идентификатор получателя сообщения
        :param message_text: текст отправляемого сообщения
        """
        if not self.authorized:
            print("Unauthorized. Check if ACCESS_TOKEN is valid")
            return

        # если не указан ID - берём значение по умолчанию, если таковое указано в .env-файле
        if receiver_user_id is None:
            receiver_user_id = self.default_user_id

        try:
            self.vk_api_access.messages.send(user_id=receiver_user_id, message=message_text, random_id=get_random_id())
            print(f"Сообщение отправлено для ID {receiver_user_id} с текстом: {message_text}")
        except Exception as error:
            print(error)


class ScheduledBot(Bot):
    """
    Бот, отправляющий сообщения по расписанию (подходит для рассылок)
    Наследуется от класса Bot
    """

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

    def __init__(self):
        """
        Иинициализация бота, работающего по расписанию
        """
        super().__init__()

        # создание расписания отправки сообщений
        self.create_schedule()

        # отправка сообщения заданному пользователю по расписанию
        while True:
            schedule.run_pending()

    def wish_good_morning(self):
        """
        Отправка случайного пожелания доброго утра
        Сообщение будет отправлено пользователю с default_user_id (можно изменить при вызове функци отправки сообщения)
        """
        pet_name = self.pet_names[random.randint(0, len(self.pet_names) - 1)]
        phrases = [
            "Доброе утро, {}! Как спалось?".format(pet_name),
            "Утро, {}! Какой план у тебя на день?".format(pet_name),
            "утро, {}".format(pet_name),
            "доброе утро, {}, какой сон тебе снился сегодня?".format(pet_name),
            "утро, уже позавтракал?".format(pet_name)
        ]
        message = phrases[random.randint(0, len(phrases) - 1)]
        self.send_message(message_text=message)

    def talk_about_lunch(self):
        """
        Отправка случайного сообщения про обед
        Сообщение будет отправлено пользователю с default_user_id (можно изменить при вызове функци отправки сообщения)
        """
        pet_name = self.pet_names[random.randint(0, len(self.pet_names) - 1)]
        phrases = [
            "угадай, чем я сегодня обедала, {}".format(pet_name),
            "приятного аппетита, {}!".format(pet_name),
            "а что ты любишь кушать, {}?".format(pet_name),
            "Что ты ел сегодня, {}?".format(pet_name),
        ]
        message = phrases[random.randint(0, len(phrases) - 1)]
        self.send_message(message_text=message)

    def ask_how_the_day_was(self):
        """
        Отправка случайного вопроса про то, как у собеседника идут дела
        Сообщение будет отправлено пользователю с default_user_id (можно изменить при вызове функци отправки сообщения)
        """
        pet_name = self.pet_names[random.randint(0, len(self.pet_names) - 1)]
        phrases = [
            "как твой день проходит, {}?".format(pet_name),
            "чем занимался сегодня, {}?".format(pet_name),
            "Признавайся, что делал весь день, {}?".format(pet_name),
            "чего успел натворить за сегодня, {}?".format(pet_name)
        ]
        message = phrases[random.randint(0, len(phrases) - 1)]
        self.send_message(message_text=message)

    def wish_good_night(self):
        """
        Отправка случайного пожелания на ночь
        Сообщение будет отправлено пользователю с default_user_id (можно изменить при вызове функци отправки сообщения)
        """
        pet_name = self.pet_names[random.randint(0, len(self.pet_names) - 1)]
        phrases = [
            "Доброй ночи, {}!".format(pet_name),
            "Сладких снов, {})".format(pet_name),
            "спи крепко, {}".format(pet_name),
            "спокнойно ночи тебе, {}, завтра продолжим".format(pet_name)
        ]
        message = phrases[random.randint(0, len(phrases) - 1)]
        self.send_message(message_text=message)

    def create_schedule(self):
        """
        Создание расписания отправки сообщений со случайным временем в заданном промежутке
        Используется время сервера
        Документация библиотеки schedule: https://schedule.readthedocs.io/en/stable/index.html
        """

        # отправка сообщения в утренние часы в случайный момент
        morning_time = "0" + str(random.randint(7, 9)) + ":" + str(random.randint(10, 59))
        schedule.every().day.at(morning_time).do(self.wish_good_morning)

        # отправка сообщения в обеденное время в случайный момент
        lunch_time = str(random.randint(11, 13)) + ":" + str(random.randint(10, 59))
        schedule.every().day.at(lunch_time).do(self.talk_about_lunch)

        # отправка сообщения в вечернее время в случайный момент
        evening_time = str(random.randint(18, 20)) + ":" + str(random.randint(10, 59))
        schedule.every().day.at(evening_time).do(self.ask_how_the_day_was)

        # отправка сообщения поздним вечером в случайный момент
        night_time = str(random.randint(22, 23)) + ":" + str(random.randint(10, 59))
        schedule.every().day.at(night_time).do(self.wish_good_night)

        # перезапуск формирования случайного расписания ровно в полночь
        schedule.every().day.at("00:00").do(self.restart_schedule)

        # вывод созданного расписания
        print(f"Расписание на {time.strftime('%d.%m.%Y')}:"
              f"\n{morning_time}\n{lunch_time}\n{evening_time}\n{night_time}\n")

    def restart_schedule(self):
        """
        Перезапуск расписания для обновления случайного времени отправки сообщений
        """
        schedule.clear()
        self.create_schedule()


if __name__ == '__main__':

    # создание и запуск бота, отправляющего сообщения по расписанию
    scheduled_bot = ScheduledBot()
