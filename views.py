from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from utils import build_menu
from dialog_manager import DialogManager



def send_speech(bot, chat_id, speech_id):
    try:
        speech = DialogManager.get_speech(speech_id)
    except StopIteration:
        speech = DialogManager.get_first_speech()

    button_list = [InlineKeyboardButton(option['text'],
                                        callback_data=str(option['reference'])
                                        )
                   for option in speech['options']
                   ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(chat_id=chat_id,
                     text=speech['text'],
                     reply_markup=reply_markup)


def hello_message(bot, update):
    send_speech(bot, update.message.chat_id, DialogManager.first_speech)


def dialog_callback_handler(bot, update):
    chat_id = update.callback_query.message.chat_id
    speech_id = update.callback_query.data

    send_speech(bot, chat_id, speech_id)

def dialog_handler(bot, update):
    chat_id = update.message.chat_id
    speech_id = update.message.text

    send_speech(bot, chat_id, speech_id)
