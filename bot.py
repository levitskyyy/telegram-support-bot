import aiogram
import config
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentType, Message

bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)


@dp.message_handler()
async def filter_messages(message: types.Message):
    if message.from_user.username in config.SUPPORT_USERNAMEs:
        if message.reply:
            text = message.text
            parse_msg = message.reply_to_message.text.replace(f'{config.USER_ID}', '')
            await bot.send_message(parse_msg, text)
    elif message.text == "/start":
        await message.answer(random.choice(config.START))
    else:
        await bot.forward_message(chat_id=config.SUPPORT_CHAT_IDs, from_chat_id=message.chat.id, message_id=message.message_id)
        await bot.send_message(config.SUPPORT_CHAT_IDs, f"{config.USER_ID}{message.chat.id}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)