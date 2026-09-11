import logging, sqlite3, datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import ReplyKeyboardMarkup

BOT_TOKEN = "8864161061:AAEG2Egytv1N0Slbc0WfCwxWEXxPTehpXMw"
OWNER_ID = 0

def main_kb():
    return ReplyKeyboardMarkup([["🧠 دردشة","📖 قرآن"],["📥 تحميل","🎮 ألعاب"],["👑 المالك"]], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global OWNER_ID
    if OWNER_ID==0:
        OWNER_ID=update.effective_user.id
    await update.message.reply_text(f"👑 أهلا {update.effective_user.first_name}! البوت الأسطوري شغال!", reply_markup=main_kb())

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"فهمتك: {update.message.text}\nأنا جاهز!", reply_markup=main_kb())

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot running")
    app.run_polling()

if __name__ == "__main__":
    main()
