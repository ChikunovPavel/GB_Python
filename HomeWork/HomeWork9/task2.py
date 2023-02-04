# 2) Создайте Бота для игры с конфетами человек против бота. (Дополнительно)
from telegram import Bot
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, ConversationHandler 

token1 =  '5929818528:AAGNO-hZgy6phFuMTC8JVdEH1nyT4Zj3oOg'

a = 0 # куча
b = 1 #чел
c = 2 #бот


bot = Bot(token = token1)
updater = Updater(token = token1)
dispather = updater.dispatcher



def game(update,context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id,"сколько конфет в коробке?")
    return a

def human(update,contex):
    text = update.message.text
    contex.bot.send_message(update.effective_chat.id,'Введи количество конфет которое хочешь взять')
    return b

def gamebot(update,context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id,"я достал из коробки ")
    return c



def cancel(update,context):
    context.bot.send_message(update.effective_chat.id,"что то пошло не так  ")


game_handler = CommandHandler('start',game)
human_handler = MessageHandler(Filters.text,human)
gamebot_handler = MessageHandler(Filters.text,gamebot)
cancel_handler = CommandHandler('cancel', cancel)


conv_handler = ConversationHandler(
    
        entry_points = [game_handler], states = {a:[human_handler] ,b:[gamebot_handler]},fallbacks = [cancel_handler])


dispather.add_handler(conv_handler)


updater.start_polling() 
updater.idle()