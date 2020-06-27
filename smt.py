import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import random
import time
import os
import sqlite3 as sq
API_TOKEN = '1133381423:AAEytfr8xb5xoB9iewgDWPAwKZlMgkArW_w'

# Configure logging
logging.basicConfig(level=logging.INFO)


class TS(Helper):
    mode = HelperMode.snake_case
    T_S1 = ListItem()
    T_S2 = ListItem()
    T_S3 = ListItem()


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

a = 0
ct = ' pip'
usid = 0
wlis = ['859850095', '898287979']

con = sq.connect(':memory:')
c = con.cursor()
c.execute("CREATE TABLE em(id integer, pol integer)")
con.commit()

con1 = sq.connect(':memory:')
c1 = con1.cursor()
c1.execute("CREATE TABLE om(id integer, p1 integer,p2 integer,p3 integer,p4 integer,p5 integer,p6 integer,p7 integer,p8 integer,p9 integer,p10 integer,p11 integer,p12 integer,p13 integer,p14 integer,p15 integer,p16 integer,p17 integer,p18 integer,p19 integer,p20 integer,p21 integer,p22 integer)")
con1.commit()

@dp.message_handler(commands=['dik'])
async def echo(message: types.Message):
    if str(message.from_user.id) in wlis:
        a = random.randint(1, 1000)
        id = '@' + str(message.from_user.username)
        text = "Уго,  " + id + " ! Твой писка целых " + str(a) + " световых лет!"
        await message.answer(text)
    else:
        a = random.randint(-200, 40)
        if (a == 0):
            text = "Не ма писка"
            id = '@' + str(message.from_user.username)
            text = id + ' ' + text
            await message.answer(text)

        if (a < 0):
            text = "Неправильна писка, всего " + str(a) + " мм!"
            id = '@' + str(message.from_user.username)
            text = id + ' ' + text
            await message.answer(text)

        if (a > 0):
            text = "Твой писка " + str(a) + " мм!"
            id = '@' + str(message.from_user.username)
            text = id + ' ' + text
            await message.answer(text)


@dp.message_handler(commands=['an_dik'])
async def check(message: types.message):
    try:
        if str(message.reply_to_message.from_user.id) in wlis:
            a = random.randint(1, 1000)
            id = '@' + str(message.reply_to_message.from_user.username)
            text = "Уго! У " + id + " писка целых " + str(a) + " световых лет!"
            await message.answer(text)
        else:
            a = random.randint(-200, 40)
            if (a < 0):
                id = '@' + str(message.reply_to_message.from_user.username)
                text = "У " + id + " Неправильна писка, всего " + str(a) + " мм!"
                await message.answer(text)
            if (a == 0):
                id = '@' + str(message.reply_to_message.from_user.username)
                text = "У " + id + " не ма писка"
                await message.answer(text)
            if (a > 0):
                id = '@' + str(message.reply_to_message.from_user.username)
                text = "У " + id + " писка " + str(a) + " мм!"
                await message.answer(text)
    except:
        await message.answer('Команда должна являться ответом на сообщение!')


@dp.message_handler(commands=['per_dik'])
async def check(message: types.message):
    try:
        if str(message.reply_to_message.forward_from.id) in wlis:
            id = '@' + str(message.reply_to_message.forward_from.username)
            a = random.randint(1, 1000)
            text = "Уго! У " + id + " писка целых " + str(a) + " световых лет!"
            await message.answer(text)
        else:
            a = random.randint(-200, 40)
            if (a < 0):
                id = '@' + str(message.reply_to_message.forward_from.username)
                text = "У " + id + " Неправильна писка, всего " + str(a) + " мм!"
                await message.answer(text)
            if (a == 0):
                id = '@' + str(message.reply_to_message.forward_from.username)
                text = "У " + id + " не ма писка"
                await message.answer(text)
            if (a > 0):
                id = '@' + str(message.reply_to_message.forward_from.username)
                text = "У " + id + " писка " + str(a) + " мм!"
                await message.answer(text)
    except:
        await message.answer(
            'Невозможно получить username человека, его профиль  закрыт или команда не является ответом на пересланное сообщение')


@dp.message_handler(commands=['whois'])
async def whois(msg: types.message):
    try:
        if msg.reply_to_message.forward_from:
            fwd = msg.reply_to_message.forward_from.id
            await msg.answer(str(fwd))
        elif msg.reply_to_message.from_user:
            fwd = msg.reply_to_message.from_user.id
            await msg.answer(str(fwd))
    except:
        fwd = msg.from_user.id
        await msg.answer(str(fwd))


@dp.message_handler(commands=['print'])
async def pr(msg: types.message):
    global ct
    await msg.answer_photo(
        'https://raw.githubusercontent.com/pvpender/tg_test_bot/master/21-11-37-1569325738_mi-mix-alpha.jpeg')


@dp.message_handler(state='*', commands=['izm'])
async def izm(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(TS.all()[1])
    await msg.answer('heh')


@dp.message_handler(state=TS.T_S2)
async def izmen(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    global ct
    ct = msg.text
    await state.reset_state()
    await msg.answer('gotov')


@dp.message_handler(lambda m: m.chat.type == 'private', state='*', commands=['sviz'])
async def otp(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(TS.all()[0])
    await msg.answer(
        'Пожалуйста, отправте ваше предложение ОДНИМ сообщением. Если сообщение успешно отправиться - вам придёт об этом сообщение. Если нет - попробуйте ещё раз. ВНИМАНИЕ: команда не работает корректно в групповых чатах, пишите боту в личное сообщение!')

@dp.message_handler(lambda m: m.chat.type != 'private', state='*', commands=['sviz'])
async def mistake(msg: types.message):
    await msg.answer('Команду /sviz нужно писать боту в личные сообщения!')

@dp.message_handler(state=TS.T_S1)
async def otpravka(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    c.execute("INSERT INTO em(id, pol) VALUES(?,?)",(msg.message_id, msg.from_user.id))
    print(msg.message_id)
    print(msg.from_user.id)
    await msg.forward(898287979)
    await state.reset_state()
    await msg.answer('Спасибо за ваше предложение! Команда поддержки рассмотрит его!')

@dp.message_handler(commands=['otv'])
async def ot(msg: types.message):
    state = dp.current_state(user= msg.from_user.id)
    global usid
    usid = msg.reply_to_message.message_id
    await state.set_state(TS.all()[2])
    await msg.answer('Ответьте на сообщение пользователя')

    @dp.message_handler(state=TS.T_S3)
    async def to(msg):

        c.execute("SELECT pol FROM em WHERE id =?",(usid-1,))
        row = c.fetchone()
        print(usid)
        print(row)
        r = row[0]
        await bot.send_message(r,msg.text)
        await state.reset_state()
        await msg.answer('gotovo')




@dp.message_handler(commands= ['dikruletka'])
async def rul(message: types.message):
 a = random.randint(1,1000)
 e = message.from_user.id
 c1.execute("SELECT id FROM om WHERE id = ?",(e,))
 r = c1.fetchone()
 if r == None:
     c1.execute("INSERT INTO om(id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22) VALUES(?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)",(e,))
 if (a>2) & (a<12):
    await message.answer('Мм... Вы  выбили обычную письку 🥔"Мистер картошка"🥔')
    c1.execute("SELECT p1 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p1 =? WHERE id = ?", (row[0] + 1, e))
 elif a == 1:
    await message.answer('Ого! Вы выбили легендарную письку 💀"Х*ёвая смерть"💀')
    c1.execute("SELECT p2 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p2 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>13) & (a<23):
    await message.answer('Мм... Вы выбили обычную письку 😷"Коронавирус"😷')
    c1.execute("SELECT p3 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p3 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>24) & (a<34):
    await message.answer('Мм... Вы выбили обычную письку 🐧"Дурка Пингвина"🐧')
    c1.execute("SELECT p4 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p4 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>35) & (a<45):
    await message.answer('Мм... Вы выбили обычную письку 🤬"Гопник"🤬')
    c1.execute("SELECT p5 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p5 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>46) & (a<56):
    await message.answer('Мм... Вы выбили обычную письку письку 🕵🏼‍♂"Каттани"🕵🏼‍♂')
    c1.execute("SELECT p6 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p6 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>57) & (a<67):
    await message.answer('Мм... Вы выбили обычную письку 🐝"Электрический улей"🐝')
    c1.execute("SELECT p7 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p7 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>68) & (a<69):
    await message.answer('Ого! Вы выбили легендарную письку 🐲"Золотой дракон"🐲')
    c1.execute("SELECT p8 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p8 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>70) & (a<76):
    await message.answer('О! Вы выбили эпич. письку 🦅"Хабиб"🦅')
    c1.execute("SELECT p9 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p9 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>77) & (a<83):
    await message.answer('О! Вы выбили эпич. письку 🎲"Азарт"🎲')
    c1.execute("SELECT p10 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p10 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>84) & (a<89):
    await message.answer('Ух! Вы выбили мифич. письку 👑"Король"👑')
    c1.execute("SELECT p11 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p11 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>90) & (a<91):
    await message.answer('Ого! Вы выбили легендарную письку 🌈"Обдавбався"🌈')
    c1.execute("SELECT p12 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p12 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>92) & (a<97):
    await message.answer('Ох! Вы выбили особенную письку 👴🏿"Флойд"👴🏿 ')
    c1.execute("SELECT p13 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p13 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>98) & (a<103):
    await message.answer('Ух! Вы выбили мифич. письку 🧻"Ценный ресурс"🧻')
    c1.execute("SELECT p14 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p14 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>104) & (a<109):
    await message.answer('Ох! Вы выбили особенную письку 🏳‍🌈"Трубочист"🏳‍🌈')
    c1.execute("SELECT p15 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p15 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>110) & (a<115):
    await message.answer('Ух! Вы выбили мифич. письку ❓"Хто я?"❓')
    c1.execute("SELECT p16 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p16 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>116) & (a<126):
    await message.answer('Хах! Вы выбили письку победителя конкурса 🇦🇶"Пингвин Дениска ебать"🇦🇶')
    c1.execute("SELECT p17 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p17 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>127) & (a<137):
    await message.answer('Хах! Вы выбили письку победителя конкурса 👴"Пожилой дед Шер"👴')
    c1.execute("SELECT p18 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p18 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>138) & (a<146):
    await message.answer('Хм... Вы выбили редкую письку 🚀"Space Ч."🚀')
    c1.execute("SELECT p19 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p19 =? WHERE id = ?", (row[0] + 1, e))
 elif (a>147) & (a<155):
    await message.answer('Хм... Вы выбили редкую письку 🧠"Мозговой штурм"🧠 ')
    c1.execute("SELECT p20 FROM om WHERE id =?", (e,))
    row = c1.fetchone()
    c1.execute("UPDATE om SET p20 =? WHERE id = ?", (row[0] + 1, e))
 elif (a > 156) & (a < 164):
     await message.answer('Хм... Вы выбили редкую письку 🃏"Цицерон"🃏')
     c1.execute("SELECT p21 FROM om WHERE id =?", (e,))
     row = c1.fetchone()
     c1.execute("UPDATE om SET p21 =? WHERE id = ?", (row[0] + 1, e))
 elif (a > 165) & (a < 173):
     await message.answer('Хм... Вы выбили редкую письку ⚱️"Антиквариат"⚱️')
     c1.execute("SELECT p22 FROM om WHERE id =?",(e,))
     row = c1.fetchone()
     c1.execute("UPDATE om SET p22 =? WHERE id = ?",(row[0]+1,e))
 else:
     await message.answer('ничего!')


@dp.message_handler(commands=['inventory'])
async def inv(msg: types.message):
    e = msg.from_user.id
    try:
        c1.execute("SELECT * FROM om WHERE id=?",(e,))
        row = c1.fetchone()
        s = "%(1)i %(2)i %(3)i %(4)i %(5)i %(6)i"%{"1":row[0], "2":row[1], "3":row[2], "4":row[3], "5":row[4], "6":row[5]}
        await msg.answer(s)
    except:
        await msg.answer('вы ещё ни разу не крутили!')
'''@dp.message_handler(state='*',commands= ['st'])
async def st(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    await state.reset_state()
    await msg.answer('st')'''
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
