
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🛍️ Katalog'
balance = '💰 Balans'
cart = '🛒 Savatcha'
delivery_status = '🚚 Buyurtma xolati'

settings = '⚙️ Настройка каталога'
orders = '🚚 Заказы'
questions = '❓ Вопросы'

@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Admin menyusiga xush kelibsiz', reply_markup=markup)

@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
    markup.add(catalog)
    markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Menyuga hush kelibsiz', reply_markup=markup)
