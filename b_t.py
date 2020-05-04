import aiogram as ai
import logging
import random
TOKEN='1133381423:AAEytfr8xb5xoB9iewgDWPAwKZlMgkArW_w'
def rand():
    a=random.randint(1,100)
    time.sleep(0.5)
    rand()


logging.basicConfig(level=logging.INFO )
bot=ai.Bot(token=TOKEN)
dp=ai.Dispatcher(bot )
@dp.message_handler(commands=['start'])
async def send_mes(message: ai.types.message):
    await message.answer(a)
    a=random.randint(1,100)


if __name__ =='__main__':
   
    ai.executor.start_polling(dp, skip_updates= True )
    rand()
