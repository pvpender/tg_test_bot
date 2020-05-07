
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



# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage= MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

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
@dp.message_handler(state='*', commands= ['sviz'])
async def otp(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(TS.all()[0])
    await msg.answer('Пожалуйста, отправте ваше предложение ОДНИМ сообщением. Если сообщение успешно отправиться - вам придёт об этом сообщение. Если нет - попробуйте ещё раз.')



@dp.message_handler(state=TS.T_S1)
async def otpravka(msg: types.message):
     state = dp.current_state(user=msg.from_user.id)
     await msg.answer(msg.text)
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

