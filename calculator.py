import logging
import re

from telegram import Update
from telegram.ext import ContextTypes


from never_share import BOT_KEY
from complex import Complex
from rational import Rational


async def rational_solution(update: Update, context: ContextTypes.DEFAULT_TYPE):
    format_error = "Didn't recognize number this time!"
    note_on_rational = "rational parsing and result here!"
    operators = ["\%", "\/\/", "\+", "\-", "\*", "\/"]
    expression = update.message['text'].lower().strip('/rational').strip()
    roots = re.split('|'.join(operators),expression)
    operators = operators = re.findall('|'.join(operators), expression)
    if len(operators) != 1 or len(roots) != 2:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=format_error)
        return
    operator = operators[0]
    numbers = (
        Rational(roots[0]),
        Rational(roots[1]))
    match operator:
        case "+":
            response = numbers[0] + numbers[1]
        case "-":
            response = numbers[0] - numbers[1]
        case "*":
            response = numbers[0] * numbers[1]
        case "/":
            response = numbers[0] / numbers[1]
        case "%":
            response = numbers[0] % numbers[1]
        case "//":
            response = numbers[0] // numbers[1]
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"it equals {response}")


async def complex_solution(update: Update, context: ContextTypes.DEFAULT_TYPE):
    format_error = "Didn't recognize number this time!"
    operators = ["\+", "\-", "\*", "\/"]
    expression = update.message['text'].lower().strip('/complex').strip()
    roots = re.split('|'.join(operators), expression)
    operators = re.findall('|'.join(operators), expression)
    if len(operators) != 3 or len(roots) != 4:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=format_error)
        return
    operator = operators[1]
    numbers = (
        Complex(roots[0]+operators[0]+roots[1]),
        Complex(roots[2]+operators[2]+roots[3]))
    match operator:
        case "+":
            response = numbers[0] + numbers[1]
        case "-":
            response = numbers[0] - numbers[1]
        case "*":
            response = numbers[0] * numbers[1]
        case "/":
            response = numbers[0] / numbers[1]
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"it equals {response}")
