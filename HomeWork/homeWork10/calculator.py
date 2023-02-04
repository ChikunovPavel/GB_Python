from telegram import Bot
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,ConversationHandler
from controllers import process_func

bot = Bot(token = '5929818528:AAGNO-hZgy6phFuMTC8JVdEH1nyT4Zj3oOg')
updater = Updater(token= '5929818528:AAGNO-hZgy6phFuMTC8JVdEH1nyT4Zj3oOg')
dispatcher = updater.dispatcher


def start(update,context):
    context.bot.send_message(update.effective_chat.id,"Привет это канкулятор введи данные которые нужно посчитать")
    

def call(update,context):
    # update.message.text
    final_data = process_func(update.message.text)
    # sum = run(update.message.text)
    context.bot.send_message(update.effective_chat.id,f' результат: {final_data}')
    return ConversationHandler.END




start_handler = CommandHandler('start', start)
call_handler = MessageHandler(Filters.text,call)







dispatcher.add_handler(start_handler)
dispatcher.add_handler(call_handler)


updater.start_polling() 
updater.idle()
