from telebot import TeleBot
from telebot.custom_filters import StateFilter
from telebot.storage import StateMemoryStorage
from  config import TOKEN
from database import DataBase

db = DataBase()
bot = TeleBot(TOKEN, state_storage=StateMemoryStorage())
bot.add_custom_filter(custom_filter=StateFilter(bot))