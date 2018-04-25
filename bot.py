# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)
allmes=[]
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.text == "show":
        bot.send_message(message.chat.id, allmes)
    else if message.text=="Настя":
        bot.send_message(message.chat.id, ' {who} {fam}!, твой костю топ, Ты просто секс'.format(who=message.from_user.first_name,fam=message.from_user.last_name))
       
    else:
        bot.send_message(message.chat.id, 'привет, {who} {fam}!, твой костю топ'.format(who=message.from_user.first_name,fam=message.from_user.last_name))
        allmes.append(message.text)
    


if __name__ == '__main__':
     bot.polling(none_stop=True)
