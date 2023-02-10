

import logging
import re

from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler,\
    ContextTypes


from never_share import BOT_KEY
from complex import Complex
from rational import Rational
from calculator import complex_solution, rational_solution


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    note_on_start = "That is calculator for two rational or two complex"\
        + " numbers. Binary operators + - * / are supported for both"\
        + " scenarios. Rational numbers also support % and //.\n"\
        + "/help for more."
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=note_on_start)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    note_on_help = "/start for intro.\n"\
        + "/complex {number1}{operator}{number2} #for complex numbers evaluation\n"\
        + "as in /complex 5+2i*2-3i\n"\
        + "/rational {number1}{operator}{number2}# for rational numbers evaluation"\
        + "as in /rational 50*3"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=note_on_help)