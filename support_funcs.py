

import logging
import re

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler,\
    ContextTypes


from never_share import BOT_KEY
from complex import Complex
from rational import Rational
from calculator import complex_solution, rational_solution


note_on_help = "/start for intro.\n"\
        + "/complex {number1}{operator}{number2} ~for complex numbers evaluation\n"\
        + "as in /complex 5+2i*2-3i\n"\
        + "/rational {number1}{operator}{number2} ~for rational numbers evaluation"\
        + "as in /rational 50*3"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE,
    helpmsg = note_on_help):
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
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = msg_)

async def invalid_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    default_ = "No can do."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=default_)