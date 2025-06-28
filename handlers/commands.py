from telebot.types import Message
from keyboards import dict_or_translate
from loader import bot

@bot.message_handler(commands=["start"])
def start(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Salom, {message.from_user.first_name}", reply_markup=dict_or_translate())