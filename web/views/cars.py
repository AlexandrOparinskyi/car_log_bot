from sqladmin import ModelView

from database import Car


class CarAdmin(ModelView, model=Car):
    name = "Машина"
    name_plural = "Машины"
    can_create = False

    column_list = (Car.id,
                   Car.name,
                   Car.user)
    form_columns = (Car.name,
                    Car.mark,
                    Car.model,
                    Car.year,
                    Car.color,
                    Car.mileage,
                    Car.engine_type,
                    Car.transmission_type,
                    Car.is_deleted,
                    Car.is_active,
                    Car.is_selected_main)

    column_labels = {
        Car.id: "Идентификатор авто",
        Car.name: "Название авто",
        Car.mark: "Марка",
        Car.model: "Модель",
        Car.year: "Год выпуска",
        Car.color: "Цвет",
        Car.mileage: "Пробег",
        Car.engine_type: "Тип двигателя",
        Car.transmission_type: "Тип коробки передач",
        Car.is_deleted: "Удалена",
        Car.is_active: "Активная",
        Car.is_selected_main: "Выбрана основной",
        Car.created_at: "Дата создания",
        Car.user: "Владелец"
    }

    column_details_list = (Car.user,
                           Car.id,
                           Car.name,
                           Car.mark,
                           Car.model,
                           Car.year,
                           Car.color,
                           Car.engine_type,
                           Car.transmission_type,
                           Car.mileage,
                           Car.is_deleted,
                           Car.is_active,
                           Car.is_selected_main,
                           Car.created_at)

    column_formatters = {
        Car.user: lambda m, a: f"{m.user.first_name} ({m.user.id})"
    }
    column_formatters_detail = {
        Car.created_at: lambda m, a: m.created_at.strftime("%d.%m.%Y %H:%M"),
        Car.user: lambda m, a: f"{m.user.first_name} ({m.user.id})"
    }
