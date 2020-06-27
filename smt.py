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
 if (a>2) & (a<12):
  await message.answer('Мм... Вы  выбили обычную письку 🥔"Мистер картошка"🥔')
 elif a == 1:
  await message.answer('Ого! Вы выбили легендарную письку 💀"Х*ёвая смерть"💀')
 elif (a>13) & (a<23):
  await message.answer('Мм... Вы выбили обычную письку 😷"Коронавирус"😷')
 elif (a>24) & (a<34):
  await message.answer('Мм... Вы выбили обычную письку 🐧"Дурка Пингвина"🐧')
 elif (a>35) & (a<45):
  await message.answer('Мм... Вы выбили обычную письку 🤬"Гопник"🤬')
 elif (a>46) & (a<56):
  await message.answer('Мм... Вы выбили обычную письку письку 🕵🏼‍♂"Каттани"🕵🏼‍♂')
 elif (a>57) & (a<67):
  await message.answer('Мм... Вы выбили обычную письку 🐝"Электрический улей"🐝')
 elif (a>68) & (a<69):
  await message.answer('Ого! Вы выбили легендарную письку 🐲"Золотой дракон"🐲')
 elif (a>70) & (a<76):
  await message.answer('О! Вы выбили эпич. письку 🦅"Хабиб"🦅')
 elif (a>77) & (a<83):
  await message.answer('О! Вы выбили эпич. письку 🎲"Азарт"🎲')
 elif (a>84) & (a<89):
  await message.answer('Ух! Вы выбили мифич. письку 👑"Король"👑')
 elif (a>90) & (a<91):
  await message.answer('Ого! Вы выбили легендарную письку 🌈"Обдавбався"🌈')
 elif (a>92) & (a<97):
  await message.answer('Ох! Вы выбили особенную письку 👴🏿"Флойд"👴🏿 ')
 elif (a>98) & (a<103):
  await message.answer('Ух! Вы выбили мифич. письку 🧻"Ценный ресурс"🧻')
 elif (a>104) & (a<109):
  await message.answer('Ох! Вы выбили особенную письку 🏳‍🌈"Трубочист"🏳‍🌈')
 elif (a>110) & (a<115):
  await message.answer('Ух! Вы выбили мифич. письку ❓"Хто я?"❓')
 elif (a>116) & (a<126):
  await message.answer('Хах! Вы выбили письку победителя конкурса 🇦🇶"Пингвин Дениска ебать"🇦🇶')
 elif (a>127) & (a<137):
  await message.answer('Хах! Вы выбили письку победителя конкурса 👴"Пожилой дед Шер"👴')
 elif (a>138) & (a<146):
  await message.answer('Хм... Вы выбили редкую письку 🚀"Space Ч."🚀')
 elif (a>147) & (a<155):
  await message.answer('Хм... Вы выбили редкую письку 🧠"Мозговой штурм"🧠 ')
 elif (a > 156) & (a < 164):
     await message.answer('Хм... Вы выбили редкую письку 🃏"Цицерон"🃏')
 elif (a > 165) & (a < 173):
     await message.answer('Хм... Вы выбили редкую письку ⚱️"Антиквариат"⚱️')
 else:
     await message.answer('ничего!')

'''@dp.message_handler(state='*',commands= ['st'])
async def st(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    await state.reset_state()
    await msg.answer('st')'''
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
