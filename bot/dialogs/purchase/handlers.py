from datetime import date

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, Button

from bot.states import PurchaseState, HomeState
from bot.utils import (get_car_by_id,
                       save_purchase,
                       replace_dot_at_comma,
                       get_user_by_id)


async def enter_purchase_total_price(message: Message,
                                     widget: MessageInput,
                                     dialog_manager: DialogManager):
    user = await get_user_by_id(message.from_user.id)
    m_text = replace_dot_at_comma(message.text)
    dialog_manager.dialog_data.update(total_price=m_text,
                                      quantity=1,
                                      user_id=user.id)

    await dialog_manager.switch_to(state=PurchaseState.edit_menu)


async def edit_purchase_params(callback: CallbackQuery,
                               widget: Select,
                               dialog_manager: DialogManager,
                               item_id: str):
    dialog_manager.dialog_data.update(purchase_param=item_id)

    if item_id == "car":
        await dialog_manager.switch_to(state=PurchaseState.edit_to_button)
        return

    if item_id == "date":
        await dialog_manager.switch_to(state=PurchaseState.calendar)
        return

    await dialog_manager.switch_to(state=PurchaseState.edit_to_text)


async def purchase_edit_car(callback: CallbackQuery,
                            widget: Select,
                            dialog_manager: DialogManager,
                            item_id: str):
    car = await get_car_by_id(int(item_id))
    dialog_manager.dialog_data.update(car=car)

    await dialog_manager.switch_to(state=PurchaseState.edit_menu)


async def enter_purchase_param(message: Message,
                               widget: MessageInput,
                               dialog_manager: DialogManager):
    purchase_param = dialog_manager.dialog_data.get("purchase_param")
    m_text = message.text

    if purchase_param in ("total_price", "price_per_unit"):
        m_text = replace_dot_at_comma(m_text)

    dialog_manager.dialog_data[purchase_param] = m_text

    await dialog_manager.switch_to(state=PurchaseState.edit_menu)


async def purchase_edit_calendar(callback: CallbackQuery,
                                   widget,
                                   dialog_manager: DialogManager,
                                   selected_date: date):
    dialog_manager.dialog_data.update(date=selected_date)

    await dialog_manager.switch_to(state=PurchaseState.edit_menu)


async def save_purchase_button(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    await callback.answer("✅ Покупка добавлена")
    await save_purchase(**dialog_manager.dialog_data)

    await dialog_manager.start(state=HomeState.home)
