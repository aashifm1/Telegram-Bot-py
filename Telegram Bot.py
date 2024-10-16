from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

Token = " " 


app = ApplicationBuilder().token(Token).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to Course Master. Use /help command to see all features")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /start -> Welcome to the Page
        /help -> It executes this message
        /C -> Gives C course link
        /CPP -> Gives C++ course link
        /Python -> Gives Python course link
        /Java -> Gives Java course link
        /SQL -> Gives SQL course link
        """
    )

async def C(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for C: https://www.udemy.com/course/c-programming-for-beginners-/")

async def CPP(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for C++: https://www.udemy.com/course/beginning-c-plus-plus-programming/")

async def Python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for Python: https://www.udemy.com/course/learn-python-with-abdul-bari/")

async def Java(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for Java: https://www.udemy.com/course/java-programming-tutorial-for-beginners/")

async def SQL(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for SQL: https://www.udemy.com/course/the-complete-sql-bootcamp/")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sorry, I didn't understand that command. Please use /help to see the list of available commands.")

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('C', C))
app.add_handler(CommandHandler('CPP', CPP))
app.add_handler(CommandHandler('Python', Python))
app.add_handler(CommandHandler('Java', Java))
app.add_handler(CommandHandler('SQL', SQL))
app.add_handler(MessageHandler(filters.COMMAND, unknown))  

app.run_polling()



