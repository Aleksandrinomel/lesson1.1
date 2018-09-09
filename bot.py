from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings




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
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('bot is run')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
main()

