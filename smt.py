
import logging
from aiogram import Bot, Dispatcher, executor, types
import random
API_TOKEN = '1133381423:AAEytfr8xb5xoB9iewgDWPAwKZlMgkArW_w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

a=0
@dp.message_handler(commands= ['dik'])
async def echo(message: types.Message):
    a=random.randint(0,20)
    if (a==0):
        text = "Не ма писка"
        id = '@' + str(message.from_user.username)
        text = id + ' ' + text
        await message.answer(text)
    '''if (a>0):
        if (a>max):
            max=a
            text="У тебя самый большой писка, целых "+str(a)+" мм!"
            await message.answer(text)
        if (a<min):
            min=a
            text="У тебя самый маленький писка, всего "+str(a)+" мм!"
            await message.answer(text)'''
    if (a < 0):
        text = "Неправильна писка, всего " + str(a) + " мм!"
        id = '@' + str(message.from_user.username)
        text = id + ' ' + text
        await message.answer(text)

    if (a>0):
        text="Твой писка "+str(a)+" мм!"
        id='@'+str(message.from_user.username)
        text=id+' '+text
        await message.answer(text)
@dp.message_handler(commands= ['an_dik'])
async def check(message: types.message ):
    a=random.randint(-20,40)
    if (a<0):
        id = '@' + str(message.reply_to_message.from_user.username)
        text = "У "+id+" Неправильна писка, всего " + str(a) + " мм!"
        await message.answer(text)
    if(a==0):
        id = '@' + str(message.reply_to_message.from_user.username)
        text = "У "+id+ " не ма писка"
        await message.answer(text)
    if(a>0):
        id = '@' + str(message.reply_to_message.from_user.username)
        text = "У "+id+ " писка "+str(a)+" мм!"
        await message.answer(text)
@dp.message_handler(commands= ['per_dik'])
async def check(message: types.message ):
    a=random.randint(-20,40)
    if (a<0):
        id = '@' + str(message.forward_from.username)
        text = "У "+id+" Неправильна писка, всего " + str(a) + " мм!"
        await message.answer(text)
    if(a==0):
        id = '@' + str()
        text = "У "+id+ " не ма писка"
        await message.answer(text)
    if(a>0):
        id = '@' + str(message.forward_id)
        text = "У "+id+ " писка "+str(a)+" мм!"
        await message.answer(text)
@dp.message_handler(lambda m: m.reply_to_message and m.reply_to_message.forward_from, commands=['whois'])
async def whois(m: types.message):
    fwd = m.reply_to_message.forward_from
    await m.reply(str(fwd))
@dp.message_handler(commands= ['sviz'])
async def echo(message: types.Message):
    message.answer("otprav")
    await message.forward(898287979)
    await message.answer("spasibo")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

