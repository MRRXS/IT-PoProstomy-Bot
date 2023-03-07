import re

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# ініціалізація бота та диспетчера
bot = Bot(token='6000075779:AAGOY0xmq5MK9BnDK3qz3opR91qtu6dmvi4')
dp = Dispatcher(bot)

text_help_commands = """
<b>
    Базові
/start - старт бота
/help - команда, в якій є список всього функціоналу бота
/description - опис бота
        
        Взаємодіїї із користувачем
піти погуляти - піти погуляти із користувачем
поцілувати - поцілувати користувача
обійняти - обійняти користувача
прижати - прижати користувача
дати шоколадку - дати шоколадку користувачу
кохаю - користувач кохає іншого користувача
сісти на коліна - користувач сідає на коліна іншому користувачу
поцілувати за шию - користувач цілує іншого користувача за шию
засосати - користувач засосав іншого користувача
добраніч - користувач побажав надобраніч користувачеві
доброго ранку - користувач сказав доброго ранку користувачеві
       
       Ваємодії із користувачем 18+
роздягнути - користувач роздягує іншого користувача
роздягнутись - користувач роздягається перед іншим користувачем
трахнути - користувач трахає іншого користувача
відсмоктати - користувач відсмоктав іншому користувачеві
відлизати - користувач відлизав іншому 
подрочити - користувач подрочив іншому користувачеві
</b>
"""
@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def on_new_chat_members(message: types.Message):
    new_members = message.new_chat_members
    for member in new_members:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"Ласкаво присому у чат! {member.first_name}!")
# ряд простих команд
@dp.message_handler(commands=['description'])
async def description_commands_bot(message: types.Message):
    description_text = "<b>Привіт, мене звати SXCLOUD, і я телеграм бот, мій семпай це MRXXV</b>"
    await message.reply(description_text, parse_mode=types.ParseMode.HTML)
    await message.delete()
@dp.message_handler(commands=['help'])
async def help_commands_mrxxv(message: types.Message):
    await message.reply(text_help_commands, parse_mode=types.ParseMode.HTML)
    await message.delete()
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    text = "<b>Привіт, це бот MRXXV, ви можете ознайомитись із його функціоналом в /help</b>"
    await message.answer(text, parse_mode=types.ParseMode.HTML)
    await message.delete()



# ряд команд взаємодіЇ
@dp.message_handler (regexp=re.compile(r"^піти погуляти", re.IGNORECASE))
async def go_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🏃‍♂️ | {user_name} пішов погуляти із {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^поцілувати", re.IGNORECASE))
async def love_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"😘 | {user_name} поцілував(-ла) {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^обійняти", re.IGNORECASE))
async def wite_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"💞|{user_name} обійняв {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^прижати", re.IGNORECASE))
async def lover_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🤲 | {user_name} прижав {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^трахнути", re.IGNORECASE))
async def sex_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🥵 | {user_name} трахнув {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^відсмоктати", re.IGNORECASE))
async def suck_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🥵 | {user_name} відсмоктала {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^відлизати", re.IGNORECASE))
async def sucking_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🥵 | {user_name} відлизав {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^роздягнути", re.IGNORECASE))
async def s_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🥵 | {user_name} роздягнув(-ла) {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^роздягнути", re.IGNORECASE))
async def w_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🥵 | {user_name} роздягнув(-ла) {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^роздягнутись", re.IGNORECASE))
async def p_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🥵 | {user_name} роздягнувся(-лась) {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^подрочити", re.IGNORECASE))
async def t_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🥵 | {user_name} подрочив(-ла) {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^дати шоколадку", re.IGNORECASE))
async def choco_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🍫 | {user_name} дав(-ла) шоколадку {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^кохаю", re.IGNORECASE))
async def lovely_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🥰 | {user_name} кохає {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")


@dp.message_handler (regexp=re.compile(r"^сісти на коліна", re.IGNORECASE))
async def set_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"😍 | {user_name} сіла на коліна {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^поцілувати за шию", re.IGNORECASE))
async def ka_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🌚 | {user_name} поцілував(-ла) за шию {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^засосати", re.IGNORECASE))
async def ka_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"💝 | {user_name} засосав(-ла) {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^добраніч", re.IGNORECASE))
async def kak_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🌚 | {user_name} побажав(-ла) спати файно {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")

@dp.message_handler (regexp=re.compile(r"^доброго ранку", re.IGNORECASE))
async def ka_command_handler(message: types.Message):
    if message.reply_to_message is not None:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=replied_user_id)
        replied_user_name = replied_user.user.first_name
        user_name = message.from_user.first_name
        await message.answer(f"🌚 | {user_name} привітався(-ла) з початком днем {replied_user_name}")
    else:
        await message.answer("Ця команда може бути виконана лише відповідно на повідомлення іншого користувача")


# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


