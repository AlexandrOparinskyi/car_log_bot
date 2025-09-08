from aiogram_dialog import Dialog, Window

from bot.states import ServiceState

service_dialog = Dialog(
    Window(
        state=ServiceState.total_price
    )
)
