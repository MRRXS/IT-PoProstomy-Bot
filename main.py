import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import re

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token="5874949026:AAEpEtlhGNGpNzL94OFfmL9ENsS6Clgqb3s")
dp = Dispatcher(bot)

# Создаем словарь для хранения рейтинга пользователей
ratings = {}
reputation = {}
text_help = """
<em>
/start - стартова команда
/help - ознайомлення з командами 
/description - можливості бота
</em>
"""
text_description = """
<b>В можливостях бота, є рейтинг і репутація</b>
  
<b>Рейтинг</b> - <em>за активність ви отримуєте бали.
Щоб переглянути статистику,потрібно в чат написати слово "рейтинг"</em>

<b>Репутація</b> - <em>якщо вам хтось допоміг, ви можете цій людині добавити  репутації .
Щоб переглянути кількість репутації,потрібно в чат написати букву " /r "</em>
"""

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text_description, parse_mode=types.ParseMode.HTML)
    await message.delete()
@dp.message_handler(regexp=re.compile(r"^дякую", re.IGNORECASE))
async def get_reputation(message: types.Message):
    user_id = message.from_user.id
    if user_id not in reputation:
        reputation[user_id] = 0
    await message.reply('Якщо вам хтось поміг, можете йому добавити репутацію через команду /r😉')

@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def on_new_chat_members(message: types.Message):
    new_members = message.new_chat_members
    for member in new_members:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"Вітаємо у cім'ї! {member.first_name}!")

@dp.message_handler(commands=['help'])
async  def help_comand_bot(message: types.Message):
    await message.answer(text_help, parse_mode=types.ParseMode.HTML)
    await message.delete()

@dp.message_handler(regexp=re.compile(r"^репутація", re.IGNORECASE))
async def get_reputation(message: types.Message):
    user_id = message.from_user.id
    if user_id not in reputation:
        reputation[user_id] = 0
    await message.reply(f'Ваша репутація: {reputation[user_id]}')

@dp.message_handler(commands=['r'])
async def give_reputation(message: types.Message):
    user_id = message.from_user.id
    reply_to_message = message.reply_to_message
    if reply_to_message is None:
        await message.reply('Ця команда повинна бути відповіддю на повідомлення іншого користувача.')
        return
    target_user_id = reply_to_message.from_user.id
    if target_user_id == user_id:
        await message.reply('Ви не можете дати репутацію самому собі.')
        return
    if target_user_id not in reputation:
        reputation[target_user_id] = 0
    reputation[target_user_id] += 1
    await message.reply(f'Репутація користувача {reply_to_message.from_user.username} збільшена на 1.')

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer("Привіт,вітаємо у сім'ї! Я чат-бот ІТ-На хлопський розум! /help - це те, що я можу.")
    await message.delete()
# Обрабатываем команду /rating
@dp.message_handler(regexp=re.compile(r"^рейтинг", re.IGNORECASE))
async def rating_command(message: types.Message):
    # Создаем отдельный список для сортировки рейтинга
    sorted_ratings = [(k, v) for k, v in ratings.items()]
    sorted_ratings.sort(key=lambda x: x[1], reverse=True)

    # Создаем сообщение с рейтингом пользователей
    text = "<b>Рейтинг користувачів:</b>\n\n"
    for i, item in enumerate(sorted_ratings, start=1):
        text += f"{i}. {item[0]} - {item[1]}\n"

    await message.reply(text, parse_mode=ParseMode.HTML)

# Обрабатываем текстовые сообщения
@dp.message_handler()
async def text_message(message: types.Message):
    # Генерируем случайный балл для пользователя
    rating = random.randint(1, 1)

    # Добавляем балл к рейтингу пользователя
    if message.from_user.username in ratings:
        ratings[message.from_user.username] += rating
    else:
        ratings[message.from_user.username] = rating

    # Отправляем сообщение с подтверждением


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)