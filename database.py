from psycopg2 import connect
from config import DATABASE, PASSWORD, USER, HOST, PORT

class DataBase:
    def __init__(self):
        self.connect = connect(
            database=DATABASE,
            password=PASSWORD,
            user=USER,
            host=HOST,
            port=PORT
        )

    def menejer(self,sql,*args,fetchone=False,fetchall=False,commit=False):
        with self.connect as db:
            cursor = db.cursor()
            cursor.execute(sql,args)
            if fetchone:
                return cursor.fetchone()
            elif fetchall:
                return cursor.fetchall()
            elif commit:
                return db.commit()

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS words(
            word_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            telegram_id BIGINT,
            word VARCHAR(100),
            translated_word VARCHAR(100)
        )"""
        self.menejer(sql,commit=True)

    def insert_table(self,telegram_id,word,translated_word):
        sql = "INSERT INTO words(telegram_id,word,translated_word) VALUES (%s,%s,%s)"
        self.menejer(sql,telegram_id,word,translated_word, commit=True)

    def select_table(self,telegram_id):
        sql = "SELECT word, translated_word FROM words WHERE telegram_id = %s ORDER BY word_id DESC LIMIT 5"
        return self.menejer(sql, telegram_id, fetchall=True)
