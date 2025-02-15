from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                        InlineKeyboardMarkup,InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Kategoriya',callback_data='catalog')],
                                     [InlineKeyboardButton(text='Kontakt',callback_data='contact'),
                                      InlineKeyboardButton(text='Savatcha',callback_data='basket')]])

settings= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='You tube',
                                                                        url='https://www.youtube.com/watch?v=qRyFNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4')]])
cars = ['BMW','Chevrolet','Mersedens']
async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/watch?v=qRyFNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4'))
    return keyboard.adjust(2).as_markup()