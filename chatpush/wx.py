import os

from wxpy import *

basedir = os.path.abspath(os.path.dirname(__file__))


def login():
    bot = Bot(cache_path=True)
    group = bot.groups().search('群名字')[0]


def get_bot():
    bot = Bot('bot.pkl', qr_path=os.path.join(
        basedir, 'static/img/qr_code.png'), console_qr=None)
    # bot.enable_puid()
    # bot.messages.max_history = 0
    return bot


bot = get_bot()
