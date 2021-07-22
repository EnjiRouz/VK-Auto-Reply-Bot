from simple_bot import Bot
from scheduled_bot import ScheduledBot
from longpoll_bot import LongPollBot

if __name__ == '__main__':
    long_poll_bot = LongPollBot()
    long_poll_bot.run_long_poll()
