from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Programming Hub Challenges- Weekly!')

updater = Updater('450585995:AAHPMDwJKv17dw68LCk_r27PqW0cMtlDy5M')

updater.dispatcher.add_handler(CommandHandler('start', start))


updater.start_polling()
updater.idle()    