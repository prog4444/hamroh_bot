from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from config import TOKEN 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

store = MemoryStorage()

bot = Bot(TOKEN)

dp = Dispatcher(bot, storage=store)

