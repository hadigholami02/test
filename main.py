import os
import logging
from pathlib import Path

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)


def load_token() -> str:
    # اول از متغیر محیطی، بعد از فایل token.txt (که توی گیت نمی‌ره)
    token = os.environ.get("BOT_TOKEN")
    if not token:
        f = Path(__file__).parent / "token.txt"
        if f.exists():
            token = f.read_text().strip()
    if not token:
        raise SystemExit("BOT_TOKEN پیدا نشد. متغیر محیطی BOT_TOKEN یا فایل token.txt رو بساز.")
    return token


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! 👋")


async def greet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام!")


def main():
    app = ApplicationBuilder().token(load_token()).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r"(?i)سلام|salam|^hi$|^hello$"), greet))
    logging.info("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
