import telebot
from telebot import types
import mysql.connector
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
token = "5346506402:AAGDGuV_khSGh7PTFe_C-kASBgT5wPKd5g0"
bot = telebot.TeleBot(token)

db = mysql.connector.connect(
            host="hasabym.com",
            user="u1184328_telegrm",
            passwd="telegram_db1",
            port="3306",
            database="u1184328_telegrm")


def upload_pdf(message):
    try:
        if message.document:
            pdf =message.document.file_id
        
        
        
            comment = message.caption
            
            print(comment)
            cursor = db.cursor()
            sql = "INSERT INTO tbl_pdfs(pdf_data, pdf_name) VALUES (%s, %s) "
            val = (pdf, comment)
            cursor.execute(sql, val)
            db.commit()
            
            bot.send_message(message.chat.id, "PDF faýl üstünlikli ýüklendi !!!")
        
        else:
            bot.send_message(message.chat.id, "Diňe PDF ýükläň!   {0.first_name} {0.last_name}\t\t\tTäzeden synanş!".format(message.from_user, message.from_user))
    except TypeError:
        pass