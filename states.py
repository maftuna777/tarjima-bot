from telebot.states import State, StatesGroup

class TranslatorState(StatesGroup):
    word = State()


