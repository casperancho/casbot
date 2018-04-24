# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, 'привет, {who}'.format(who=message.from_user.first_name))



if __name__ == '__main__':
     bot.polling(none_stop=True)
