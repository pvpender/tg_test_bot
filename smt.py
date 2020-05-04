
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1133381423:AAEytfr8xb5xoB9iewgDWPAwKZlMgkArW_w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands= ['start'])
async def echo(message: types.Message):

    await message.answer('sds')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

