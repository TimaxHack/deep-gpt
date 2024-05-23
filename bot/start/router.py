from aiogram import types, Router
from aiogram.filters import CommandStart

from bot.gpt import change_model_command
from bot.payment import payment_command_start

startRouter = Router()

hello_text = """
👋 Привет! Я самый умный бот, я использую в себе самые мощные нейросети на данный момент!

🤖 Я готов помочь тебе с любой задачей, просто напиши сообщение! 
"""


@startRouter.message(CommandStart())
async def buy(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[
            types.KeyboardButton(text=payment_command_start()),
            types.KeyboardButton(text=change_model_command())
        ]],
        input_field_placeholder="💬 Задай свой вопрос"
    )

    await message.answer(
        text=hello_text,
        reply_markup=keyboard
    )
