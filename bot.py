# -*- coding: utf-8 -*-
import config
import telebot
token = '517924938:AAGrk3Bq9atIqSXHka1WCxGSjxDh6Mu5S2g'
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, text=' Hello {who}'.format(who=message.from_user.first_name))
    #    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
