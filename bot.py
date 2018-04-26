# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

allmes=[]
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    if message.text == "show":
        ShowAll(allmes,message.chat.id)
    elif message.text == "Настя":
        bot.send_message(message.chat.id,
                         ' {who} {fam}!, твой костюм топ, Ты просто секс'.format(who=message.from_user.first_name,
                                                                                fam=message.from_user.last_name))
    else:
        bot.send_message(message.chat.id,
                         'привет, {who} {fam}!, твой костюм топ'.format(who=message.from_user.first_name,
                                                                       fam=message.from_user.last_name))
        listAppend(allmes,message)



def NewListCreate():
    list = []
    return list


def listAppend(list,message):
    list.append(message.text)


def ShowAll(list,idc):
    bot.send_message(idc, '------all------')
    for each in allmes:
        bot.send_message(idc, each)
    bot.send_message(idc, '---------')
    print(list),


if __name__ == '__main__':
     bot.polling(none_stop=True)
