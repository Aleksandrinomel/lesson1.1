from telegram.ext import Updater , CommandHandler
import logging
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def greet_user(bot, update):
    print('вызван /start')
def main():
    mybot = Updater("652758562:AAH6g-2ij7s1Peb_ZaERljaVFSAzpY75X7U", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()

main()
