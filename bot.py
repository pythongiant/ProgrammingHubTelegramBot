from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Programming Hub Challenges- Weekly!')
def task(bot,update):    
    update.message.reply_text('Current Challenge is:')
    file=open("task.txt")
    a=file.read()    
    print(a)    
    update.message.reply_text(a)
updater = Updater('450585995:AAHPMDwJKv17dw68LCk_r27PqW0cMtlDy5M')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('task', task))

updater.start_polling()
updater.idle()    