from aiogram.fsm.state import StatesGroup, State


class StartState(StatesGroup):
    start = State()
    acquaintance = State()
    car_name = State()
    choice = State()
    edit_car_menu = State()
    edit_to_text = State()
    edit_to_button = State()
    end_acquaintance = State()


class HomeState(StatesGroup):
    home = State()


class InstructionState(StatesGroup):
    instructions = State()
    select_instruction = State()
