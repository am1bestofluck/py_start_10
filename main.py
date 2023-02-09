

import logging
import re

from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler,\
    ContextTypes


from never_share import BOT_KEY
from complex import Complex
from rational import Rational
from calculator import complex_solution, rational_solution
from support_funcs import start, help

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)





def main():
    app = Application.builder().token(BOT_KEY).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("rational", rational_solution))
    app.add_handler(CommandHandler("complex", complex_solution))
    app.run_polling()


if __name__ == "__main__":
    main()
