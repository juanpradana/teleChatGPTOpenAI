import os
from dotenv import load_dotenv
import openai
from telegram.ext import Updater, MessageHandler, Filters

# Get data from dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
token_tele = os.getenv("TOKEN")

# Authenticate with OpenAI
openai.api_key = api_key

# Create Telegram bot
updater = Updater(token=token_tele, use_context=True)

# Handle incoming messages
def handle_message(update, context):
    text = update.message.text
    # Use GPT-3 to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{text}",
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )
    # Send the response back to the user
    update.message.reply_text(response.choices[0].text)

# Start polling for new messages
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()