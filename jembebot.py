import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters


# creates a variable to store the bot token
updater = Updater(token='401734925:AAFDIy_Z48vlnf1p0LDRO7OR_olpz0m3lXc')
dispatcher = updater.dispatcher


# add logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO
)


# function for starting messages by the bot
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="i am jembebot love me and use me")


# display  sent messages back to the user
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


# this commands sends the message the user has sent back in capital letters
def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


# displays message to the user if wrong command is initiated
# warning : should be added last
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="i dont understand but i love you")


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
caps_handler = CommandHandler('caps', caps, pass_args=True)
unknown_handler = MessageHandler(Filters.command, unknown)


# adds all handlers to the dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(unknown_handler)

# starts the bot
updater.start_polling()
