# Импортируем нужные компоненты

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s -%(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                   )
def talk_to_me(update, context):
    user_text = "Hi {}! You write: {}".format(update.message.chat.first_name, update.message.text)
 #   logging.info(user_text)
    logging.info("User: %s, Chat: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text )
#    print(user_text)
#    print(update.message)
    update.message.reply_text(user_text)


def greet_user(update, context):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

# Функцичя, которая соединяется с платформой Telegram, "тело" нашего бота

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
#   mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)

    logging.info('Bot is starting')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.start_polling()
    mybot.idle()



# Запуск бота

main()
