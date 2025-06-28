from loader import bot, db
import handlers
if __name__ == "__main__":
    db.create_table()
    print("Bot ishga tushdi")
    bot.infinity_polling()
