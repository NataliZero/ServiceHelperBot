import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from config import TOKEN
from keyboards.keyboards import menu_keyboard, links_keyboard, dynamic_keyboard, dynamic_options_keyboard

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Здесь добавляем обработчики!

# Задание 1: Обработка команды /start с меню
@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Выберите действие:",
        reply_markup=menu_keyboard
    )

@dp.message(lambda message: message.text == "Привет")
async def say_hello(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(lambda message: message.text == "Пока")
async def say_goodbye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

# Задание 2: Обработка команды /links
@dp.message(lambda message: message.text == "/links")
async def send_links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=links_keyboard)

# Задание 3: Обработка команды /dynamic
@dp.message(lambda message: message.text == "/dynamic")
async def dynamic_menu(message: Message):
    await message.answer("Нажмите кнопку ниже:", reply_markup=dynamic_keyboard)

@dp.callback_query(lambda callback: callback.data == "show_more")
async def show_more_options(callback: CallbackQuery):
    await callback.message.edit_text("Выберите опцию:", reply_markup=dynamic_options_keyboard)

@dp.callback_query(lambda callback: callback.data in ["option_1", "option_2"])
async def handle_dynamic_options(callback: CallbackQuery):
    option_text = "Вы выбрали Опцию 1!" if callback.data == "option_1" else "Вы выбрали Опцию 2!"
    await callback.message.answer(option_text)
    await callback.answer()

# Основная функция запуска
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
