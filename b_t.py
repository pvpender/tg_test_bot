import aiogram as ai
import logging
import random
TOKEN='1133381423:AAEytfr8xb5xoB9iewgDWPAwKZlMgkArW_w'



logging.basicConfig(level=logging.INFO )
bot=ai.Bot(token=TOKEN)
dp=ai.Dispatcher(bot )
@dp.message_handler(commands=['start'])
async def send_mes(message: ai.types.message):
    text="Привет {random.randint(1,100)}"
    await message.answer(text)
  


if __name__ =='__main__':
   
    ai.executor.start_polling(dp, skip_updates= True )

