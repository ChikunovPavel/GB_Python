# 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# Пример:
# привет приабвет ограбпв
# Ответ:
# привет ограбпв
from telegram import Bot
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, ConversationHandler 

token1 =  '5929818528:AAGNO-hZgy6phFuMTC8JVdEH1nyT4Zj3oOg'

a = 0

bot = Bot(token = token1)
updater = Updater(token = token1)
dispather = updater.dispatcher


def start(update,context):
    context.bot.send_message(update.effective_chat.id,"Привет \nВведи текст, я помогу тебе убрать все слова где есть абв")
    return a

def privet(update,contex):
    text = update.message.text
 
    list = [i for i in text.split()]
    newlist = []
    for i in list:
        if 'абв' not in i:
            newlist.append(i)

    
    list2 = ' '.join(map(str, newlist))
    contex.bot.send_message(update.effective_chat.id,f'{list2}')
    return ConversationHandler.END

def cancel(update,context):
    context.bot.send_message(update.effective_chat.id,"что то пошло не так  ")


start_handler = CommandHandler('start', start)
privet_handler = MessageHandler(Filters.text,privet)
cancel_handler = CommandHandler('cancel', cancel)


conv_handler = ConversationHandler(entry_points = [start_handler], states = {a:[privet_handler]},fallbacks = [cancel_handler])


dispather.add_handler(conv_handler)


updater.start_polling() 
updater.idle()