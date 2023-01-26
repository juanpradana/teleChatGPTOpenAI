import os
from dotenv import load_dotenv
import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()
api_key = os.getenv("API_KEY")
token_tele = os.getenv("TOKEN")

# print(api_key + "\n" + token_tele)
# print(telegram.__version__)
def start(update, context):
    update.message.reply_text('Selamat datang di bot kami!')

def chat(update, context):
    prompt = update.message.text
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    update.message.reply_text(message)

def main():
    openai.api_key = api_key
    updater = Updater(token_tele, use_context=True)
    dp = updater.dispatcher
    print(dp)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, chat))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
