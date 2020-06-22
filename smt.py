
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.helper import  Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import  MemoryStorage
from aiogram.contrib.middlewares.logging import  LoggingMiddleware
import random
import time

API_TOKEN = '1133381423:AAEytfr8xb5xoB9iewgDWPAwKZlMgkArW_w'

# Configure logging
logging.basicConfig(level=logging.INFO)

class TS(Helper):
    mode = HelperMode.snake_case
    T_S1 =ListItem()
    T_S2 = ListItem()


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage= MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

a=0
ct = ' pip'

wlis = ['859850095', '898287979']
@dp.message_handler(commands= ['dik'])
async def echo(message: types.Message):
    if str(message.from_user.id) in wlis:
        a = random.randint(1, 1000)
        id = '@' + str(message.from_user.username)
        text = "Уго,  " + id + " ! Твой писка целых " + str(a) + " метров!"
        await message.answer(text)
    else:
     a=random.randint(-20,40)
     if (a==0):
         text = "Не ма писка"
         id = '@' + str(message.from_user.username)
         text = id + ' ' + text
         await message.answer(text)

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
    if str(message.reply_to_message.from_user.id) in wlis:
        a = random.randint(1, 1000)
        id = '@' + str(message.reply_to_message.from_user.username)
        text = "Уго! У "+id+" писка целых "+str(a)+" метров!"
        await message.answer(text)
    else:
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
    if str(message.reply_to_message.forward_from.id) in wlis:
        a = random.randint(1, 1000)
        id = '@' + str(message.reply_to_message.forward_from.username)
        text = "Уго! У "+id+" писка целых "+str(a)+" метров!"
        await message.answer(text)
    else:
     a=random.randint(-20,40)
     if (a<0):
         id = '@' + str(message.reply_to_message.forward_from.username)
         text = "У "+id+" Неправильна писка, всего " + str(a) + " мм!"
         await message.answer(text)
     if(a==0):
         id = '@' + str(message.reply_to_message.forward_from.username)
         text = "У "+id+ " не ма писка"
         await message.answer(text)
     if(a>0):
         id = '@' + str(message.reply_to_message.forward_from.username)
         text = "У "+id+ " писка "+str(a)+" мм!"
         await message.answer(text)
        
@dp.message_handler(commands=['whois'])
async def whois(msg: types.message):
    if msg.reply_to_message.forward_from:
      fwd = msg.reply_to_message.forward_from.id
      await msg.answer(str(fwd))
    elif msg.reply_to_message.from_user:
        fwd = msg.reply_to_message.from_user.id
        await msg.answer(str(fwd))
    else:
        fwd = msg.from_user.id
        await msg.answer(str(fwd))
        
@dp.message_handler(commands = ['print'])
async def pr(msg: types.message):
    global ct
    await msg.answer(ct)

@dp.message_handler(state='*', commands = ['izm'])
async def izm(msg: types.message ):
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(TS.all()[1])
    await msg.answer('heh')
@dp.message_handler(state=TS.T_S2)
async def izmen(msg=types.message):
    state = dp.current_state(user=msg.from_user.id)
    global ct
    ct = msg.text
    await state.reset_state()
    await msg.answer('gotov')


@dp.message_handler(lambda m: m.chat.type=='private',state='*', commands= ['sviz'])
async def otp(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(TS.all()[0])
    await msg.answer('Пожалуйста, отправте ваше предложение ОДНИМ сообщением. Если сообщение успешно отправиться - вам придёт об этом сообщение. Если нет - попробуйте ещё раз. ВНИМАНИЕ: команда не работает корректно в групповых чатах, пишите боту в личное сообщение!')



@dp.message_handler(state=TS.T_S1)
async def otpravka(msg: types.message):
     state = dp.current_state(user=msg.from_user.id)
     await msg.forward(898287979)
     await state.reset_state()
     await msg.answer('Спасибо за ваше предложение! Команда поддержки рассмотрит его!')


'''@dp.message_handler(state='*',commands= ['st'])
async def st(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    await state.reset_state()
    await msg.answer('st')'''
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

