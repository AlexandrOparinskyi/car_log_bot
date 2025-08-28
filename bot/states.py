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
    write_developer = State()
    select_record = State()


class InstructionState(StatesGroup):
    instructions = State()
    select_instruction = State()


class GarageState(StatesGroup):
    garage = State()
    car_info = State()
    edit_to_text = State()
    edit_to_button = State()
    delete_car = State()
    large_count_car = State()


class AddCarState(StatesGroup):
    car_name = State()
    edit_car_menu = State()
    edit_to_text = State()
    edit_to_button = State()


class RefuelState(StatesGroup):
    total_price = State()
