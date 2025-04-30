from aiogram.dispatcher.filters.state import State,StatesGroup


class KinoState(StatesGroup):

    udalit = None
    kino=State()
    kod=State()


class ReklamaState(StatesGroup):
    reklama=State()
    confirm=State()

class UchirishState(StatesGroup):
    udalit = State()

