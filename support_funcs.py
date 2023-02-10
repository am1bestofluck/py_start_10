
import datetime
import logging

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


logging.basicConfig(filename = f'./log_storage/{datetime.date.today():%d-%m-%Y}_tg.log',
level=logging.INFO, encoding='utf-8', filemode='a')


note_on_help = "/start for intro.\n"\
        + "/complex {number1}{operator}{number2} ~for complex numbers evaluation\n"\
        + "as in /complex 5+2i*2-3i\n"\
        + "/rational {number1}{operator}{number2} ~for rational numbers evaluation"\
        + "as in /rational 50*3"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE,
    helpmsg = note_on_help):
    logging.info(f"{datetime.datetime.now():%H-%M-%S}::{update.message['chat']['id']}::'{update.message['chat']['first_name']}"\
        +f" {update.message['chat']['last_name']}':: {update.message['text']}")
    helpButton = KeyboardButton("/help")
    note_on_start = "That is <b>calculator</b> , deals in exactly <b>two"\
    +" rational or two complex numbers.</b>\n"+\
        " Binary operators  + - * / are supported for both scenarios.\n"+\
        " Rational numbers also  support % and // .\n"\
        + "/help for more."
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=note_on_start, parse_mode='HTML',
        reply_markup=ReplyKeyboardMarkup([[helpButton]]))
    



async def help(update: Update, context: ContextTypes.DEFAULT_TYPE,msg_:str = note_on_help):
    logging.info(f"{datetime.datetime.now():%H-%M-%S}::{update.message['chat']['id']}::'{update.message['chat']['first_name']}"\
        +f" {update.message['chat']['last_name']}':: {update.message['text']}")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = msg_)

async def invalid_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"{datetime.datetime.now():%H-%M-%S}::{update.message['chat']['id']}::'{update.message['chat']['first_name']}"\
        +f" {update.message['chat']['last_name']}':: {update.message['text']}")
    default_ = "No can do."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=default_)