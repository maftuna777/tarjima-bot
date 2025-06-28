from telebot.types import CallbackQuery, Message
from translators.server import tss
from loader import bot, db
from keyboards import *
from states import TranslatorState

@bot.callback_query_handler(func=lambda call: call.data in ["translate","history"])
def history_or_translate(call:CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.id)
    if call.data == "translate":
        bot.send_message(chat_id, "Tarjima", reply_markup=get_buttons())
    else:
        result = db.select_table(chat_id)
        if len(result) > 0:
            text = "Lug'at\n"
            for word, translated_word in result:
                text += f"{word} - {translated_word}\n"
        else:
            text = "Lug'atingiz bo'sh!"
        bot.send_message(chat_id, text, reply_markup=dict_or_translate())

@bot.callback_query_handler(func=lambda call:call.data in ["uz_en","uz_ru","en_uz","en_ru","ru_en","ru_uz"])
def translate_word(call:CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    bot.delete_message(chat_id,call.message.id)
    from_lang, to_lang = call.data.split("_")
    if from_lang == "uz":
        text = "So'z kiriting:"
    elif from_lang == "en":
        text = "Enter a word:"
    else:
        text = "Введите слово:"
    bot.send_message(chat_id, text)
    bot.set_state(user_id, TranslatorState.word, chat_id)
    with bot.retrieve_data(user_id, chat_id) as data:
        data["from_lang"] = from_lang
        data["to_lang"] = to_lang

@bot.message_handler(content_types="text", state=TranslatorState.word)
def translator_func(message:Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    word = message.text
    with bot.retrieve_data(user_id, chat_id) as data:
        from_lang = data["from_lang"]
        to_lang = data["to_lang"]
    translated_word = tss.google(word, from_lang, to_lang)
    data["word"] = word
    data["translated_word"] = translated_word
    bot.send_message(chat_id, translated_word, reply_markup=save_or_cancel())

@bot.callback_query_handler(func=lambda call: call.data == 'save')
def save_or_ignore(call:CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        word = data["word"]
        translated_word = data["translated_word"]
    db.insert_table(chat_id, word, translated_word)
    bot.send_message(chat_id, "Saqlandi", reply_markup=dict_or_translate())



