import logging

from invoke import task
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler

from dialog_manager import DialogManager
from views import hello_message, dialog_handler, dialog_callback_handler

@task(default=True)
def start_bot(c):
    DialogManager.set_speeches(c.config.speeches, c.config.start_id)

    request_kwargs = {
        'proxy_url': c.config.proxy.url,
    }

    updater = Updater(token=c.config.token, request_kwargs=request_kwargs)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', hello_message)
    dialog = MessageHandler(Filters.text, dialog_handler)
    callback_dialog = CallbackQueryHandler(dialog_callback_handler)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(callback_dialog)
    dispatcher.add_handler(dialog)

    logging.info("Start bot..")
    updater.start_polling()