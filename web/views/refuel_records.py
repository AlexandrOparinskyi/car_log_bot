from sqladmin import ModelView

from database import RefuelRecord


class RefuelRecordAdmin(ModelView, model=RefuelRecord):
    name = "Заправка"
    name_plural = "Заправки"
    can_create = False

    column_list = (RefuelRecord.id,
                   RefuelRecord.user,
                   RefuelRecord.car,
                   RefuelRecord.total_price,
                   RefuelRecord.created_at)

    form_columns = (RefuelRecord.total_price,
                    RefuelRecord.liters,
                    RefuelRecord.price_per_liter,
                    RefuelRecord.fuel_type,
                    RefuelRecord.gas_station,
                    RefuelRecord.time,
                    RefuelRecord.full_tank,
                    RefuelRecord.comment,
                    RefuelRecord.created_at)

    column_labels = {
        RefuelRecord.id: "Идентификатор заправки",
        RefuelRecord.user: "Пользователь",
        RefuelRecord.car: "Машина",
        RefuelRecord.total_price: "Общая цена",
        RefuelRecord.price_per_liter: "Цена за литр",
        RefuelRecord.liters: "Количество литров",
        RefuelRecord.fuel_type: "Тип топлива",
        RefuelRecord.time: "Время зарядки",
        RefuelRecord.full_tank: "Полный бак",
        RefuelRecord.comment: "Комментарий",
        RefuelRecord.created_at: "Дата заправки",
    }

    column_details_list = (RefuelRecord.id,
                           RefuelRecord.user,
                           RefuelRecord.car,
                           RefuelRecord.total_price,
                           RefuelRecord.liters,
                           RefuelRecord.price_per_liter,
                           RefuelRecord.fuel_type,
                           RefuelRecord.gas_station,
                           RefuelRecord.time,
                           RefuelRecord.full_tank,
                           RefuelRecord.comment,
                           RefuelRecord.created_at)

    column_formatters = {
        RefuelRecord.created_at: lambda m, a: m.created_at.strftime("%d.%m.%Y %H:%M"),
        RefuelRecord.user: lambda m, a: f"{m.user.first_name} ({m.user.id})",
        RefuelRecord.car: lambda m, a: m.car.name,
    }
    column_formatters_detail = {
        RefuelRecord.created_at: lambda m, a: m.created_at.strftime("%d.%m.%Y %H:%M"),
        RefuelRecord.user: lambda m, a: f"{m.user.first_name} ({m.user.id})",
        RefuelRecord.car: lambda m, a: m.car.name,
        RefuelRecord.fuel_type: lambda m, a: m.fuel_type.value,
        RefuelRecord.gas_station: lambda m, a: m.gas_station.value,
    }
