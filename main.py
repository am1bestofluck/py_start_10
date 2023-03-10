

import sys

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

try:
    from never_share import BOT_KEY
except ImportError:
    print("Ключ придётся взять свой. Лежит в never_share.py под именем BOT_KEY")
    sys.exit()

from calculator import complex_solution, rational_solution
from support_funcs import start, help, invalid_input





def main():
    app = Application.builder().token(BOT_KEY).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("rational", rational_solution))
    app.add_handler(CommandHandler("complex", complex_solution))
    app.add_handler(MessageHandler(filters.ALL, invalid_input))
    app.run_polling()


if __name__ == "__main__":
    main()
