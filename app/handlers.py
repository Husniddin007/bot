from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboards as kb

from app.middlewheres import TestMiddlewhere


router = Router()

router.message.outer_middleware(TestMiddlewhere())

class Register(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'''Salom\nInfo:\nID:{message.from_user.id}\nIsm:{message.from_user.first_name}\nFamilya:{message.from_user.last_name}\nUsername:{message.from_user.username}\n''',
reply_markup=kb.main)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Qanday yordam bera olaman /help')

@router.message(F.text=='Qandaysan')
async def how(message: Message):
    await message.answer('OK')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.reply(f"ID photo {message.photo[-1].file_id}")


@router.message(Command('get_photo'))
async def get_photo(message:Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMmZ69MeheOyHC1pTysYJUWFlWslQwAAtnzMRtEr4FJWpPrclEtJuQBAAMCAAN5AAM2BA',
    caption='terminal')

@router.callback_query(F.data=='catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Kategoriya tanlang',show_alert=True)
    await callback.message.edit_text('Salom',reply_markup=await kb.inline_cars())

@router.message(Command('register'))
async def register_one(message: Message,state:FSMContext):
    await state.set_state(Register.name)
    await message.answer('Ismingizni kiriting')

@router.message(Register.name)
async def register_two(message: Message,state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.number)
    await message.answer('Nomer jonating')

@router.message(Register.number)
async def register_there(message: Message,state: FSMContext):
    await state.update_data(number=message.text)
    data= await state.get_data()
    await message.answer(f'Rahmat,royhatdan otish yakunlandi\nIsm:{data['name']}\nNumber:{data['number']}')
    await state.clear()