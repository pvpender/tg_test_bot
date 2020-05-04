import aiogram as ai
import logging
import random
TOKEN='1133381423:AAEytfr8xb5xoB9iewgDWPAwKZlMgkArW_w'


logging.basicConfig(level=logging.INFO )
bot=ai.Bot(token=TOKEN)
dp=ai.Dispatcher(bot )
menu=ai.types.ReplyKeyboardMarkup(
    keyboard=[
    [
        ai.types.KeyboardButton(text="Да")
    ],
        [
            ai.types.KeyboardButton(text="Нет")
        ]
    ], resize_keyboard=True )

@dp.message_handler(commands=['start'])
async def send_mes(message: ai.types.message):
    text = "Привет, тебе " + str(random.randint(1, 100)) + "?"
    await message.answer(text, reply_markup=menu)

@dp.message_handler(ai.dispatcher.filters.Text(equals=["Да","Нет"]))
async def ans(message: ai.types.message):
    if (message.text == "Да"):
        await message.answer("Je")


if __name__ =='__main__':
    ai.executor.start_polling(dp, skip_updates= True )
