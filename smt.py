
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
        await message.answer('Не ма писки')
    '''if (a>0):
        if (a>max):
            max=a
            text="У тебя самый большой писка, целых "+str(a)+" мм!"
            await message.answer(text)
        if (a<min):
            min=a
            text="У тебя самый маленький писка, всего "+str(a)+" мм!"
            await message.answer(text)'''
    if (a>0):
        text="Твой писка "+str(a)+" мм!"
        id=message.from_user.username
        await message.answer(id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

