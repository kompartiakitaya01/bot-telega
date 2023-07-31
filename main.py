import telebot
from random import*
import datetime

bot = telebot.TeleBot('6198124934:AAFyeu-k-3qRwJRpF6ht-0S42BETh7mAD6A')
users = {}

def pipka(bakl=0):
    d = randint(0, 20)
    if d <= 17:
        bakl += choice([7, 2, 1, 5, 9, 11, 12, 6, 8, 3, 5, 25])
    else:
        bakl -= choice([7, 2, 1, 5, 9, 11, 12, 6, 8, 3, 5, 25])
    return bakl

@bot.message_handler(commands=['start'])
def starter(ch):
    if ch.from_user.id not in users:
        print(users, 1)
        b = pipka()
        users[ch.from_user.id] = [ch.from_user.first_name, int(str(datetime.date.today()).split('-')[2]), b]
        if b >= 1:
            bot.send_message(ch.from_user.id, choice([f'твоя колыбаха вытянулась до {users[ch.from_user.id][2]}cm',
            f'прибор увеличился до {users[ch.from_user.id][2]}cm', f'твоя пиприка проросла до {users[ch.from_user.id][2]}см']))
        else:
            bot.send_message(ch.from_user.id, choice([f'твой прибор скукурузился до {users[ch.from_user.id][2]}см',
            f'увы ах, уменьшился до {users[ch.from_user.id][2]}см', f'хахах, лох, отсох до {users[ch.from_user.id][2]}см']))

    if int(str(datetime.date.today()).split('-')[2]) - users[ch.from_user.id][1] < 1:
        bot.send_message(ch.from_user.id, choice(['а на сегодня все', 'до завтра', 'завтра на этом же месте']))
    else:
        past = users[ch.from_user.id][2]
        b1 = pipka()
        b = b1 + users[ch.from_user.id][2]
        users[ch.from_user.id] = [ch.from_user.first_name, int(str(datetime.date.today()).split('-')[2]), b]
        if b >= past:
            bot.send_message(ch.from_user.id, choice([f'твоя колыбаха вытянулась до {users[ch.from_user.id][2]}cm',
            f'прибор увеличился до {users[ch.from_user.id][2]}cm',f'твоя пиприка проросла до {users[ch.from_user.id][2]}см']))
        else:
            bot.send_message(ch.from_user.id, choice([f'твой прибор скукурузился до {users[ch.from_user.id][2]}см',
            f'увы ах, уменьшился до {users[ch.from_user.id][2]}см',f'хахах, лох, отсохло до {users[ch.from_user.id][2]}см']))


@bot.message_handler(commands=['desktop'])
def desktop(ch):
    d = {}
    for key in users:
        d[users[key][2]] = users[key][0]
    s = 'топ размеров:\n'

    for key in sorted(d.keys())[::-1]:
        ds = f'{d[key]} -- {key}cm\n'
        s += ds
    bot.send_message(ch.from_user.id, s)


@bot.message_handler()
def text_pass(ch):
    pass
bot.polling(none_stop=True)

#group_id -1001695554310