from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_buttons():
    markup = InlineKeyboardMarkup()
    uz_en = InlineKeyboardButton('🇺🇿 ➡️ 🇺🇸', callback_data="uz_en")
    uz_ru = InlineKeyboardButton('🇺🇿 ➡️ 🇷🇺', callback_data="uz_ru")
    en_uz = InlineKeyboardButton('🇺🇸 ➡️ 🇺🇿', callback_data="en_uz")
    en_ru = InlineKeyboardButton('🇺🇸 ➡️ 🇷🇺', callback_data="en_ru")
    ru_uz = InlineKeyboardButton('🇷🇺 ➡️ 🇺🇿', callback_data="ru_uz")
    ru_en = InlineKeyboardButton('🇷🇺 ➡️ 🇺🇸', callback_data="ru_en")
    markup.add(uz_en,uz_ru,en_uz,en_ru,ru_uz,ru_en, row_width=2)
    return markup

def save_or_cancel():
    markup = InlineKeyboardMarkup(keyboard=[
        [InlineKeyboardButton("Save", callback_data="save")],
        [InlineKeyboardButton("Cancel", callback_data="translate")],
    ])
    return markup

def dict_or_translate():
    markup = InlineKeyboardMarkup(keyboard=[
        [InlineKeyboardButton("Dictionary", callback_data="history")],
        [InlineKeyboardButton("Translate", callback_data="translate")],
    ])
    return markup
