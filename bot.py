from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def talk_to_me(bot, update):
    user_text = "Привет {}! ti napisal: {}".format(update.message.chat.first_name, update.message.text) 
    logging.info('user: %s, chat id: %s, message: %s', update.message.chat.username, update.message.chat.id, update.message.text)

    update.message.reply_text(user_text)
    
def greet_user(bot, update):
    text = ('вызван start')
    logging.info(text)
    update.message.reply_text(text)

def main():
    mybot = Updater("652758562:AAH6g-2ij7s1Peb_ZaERljaVFSAzpY75X7U", request_kwargs=PROXY)
    
    logging.info('bot is run')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
main()

