# TODO прикрутить корпус для чат-бота и закинуть в longpoll для автоматизации ответов на частые вопросы

from longpoll_bot import LongPollBot


class NLULongPollBot(LongPollBot):

    def __init__(self):
        super().__init__()

    def run_long_poll(self):
        raise NotImplementedError("Определи run_long_poll в %s." % self.__class__.__name__)
