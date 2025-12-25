from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# گرفتن توکن از Environment Variable
TOKEN = os.getenv("BOT_TOKEN")

START_MESSAGE = """سلام :wave:
به بات ما خوش اومدی!
از منوی زیر یکی از گزینه‌ها رو انتخاب کن :point_down:"""

keyboard = [
    [":pushpin: راهنما", ":information_source: درباره ما"],
    [":telephone_receiver: پشتیبانی"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام، به پشتیبانی داب ورس خوش اومدی. اگر پیشنهادی، انتقادی و سوالی داری؛ لطفا صبر کن تا در اولین فرصت جواب بدیم",
        reply_markup=reply_markup
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "سلام":
        await update.message.reply_text("سلام! خوبی؟ :sunglasses:")
    elif text == ":pushpin: راهنما":
        await update.message.reply_text("اگر با ادمین کاری داری فقط کافیه اندکی صبر کنی :white_check_mark:")
    elif text == ":information_source: درباره ما":
        await update.message.reply_text(
            "این بات توسط henriksson(noggy) ساخته شده.\n"
            "شما میتوانید تمامی دوبلور ها به همراه کار هایشان را در https://t.me/DubVerse921 مشاهده کنید"
        )
    elif text == ":telephone_receiver: پشتیبانی":
        await update.message.reply_text("برای پشتیبانی با @TheNoggu تماس بگیر :envelope_with_arrow:")
    else:
        await update.message.reply_text("منتظر بمون تا ادمین جواب بده!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
app.run_polling()
