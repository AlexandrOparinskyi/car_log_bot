from sqladmin import ModelView

from database import User


class UserAdmin(ModelView, model=User):
    name = "Пользователь"
    name_plural = "Пользователи"
    can_create = False

    column_list = (User.id,
                   User.first_name,
                   User.last_name,
                   User.is_admin,
                   User.is_premium,
                   User.is_banned)
    form_columns = (User.first_name,
                    User.last_name,
                    User.is_admin,
                    User.is_banned,
                    User.is_premium)
    column_labels = {
        User.id: "Идентификатор чата",
        User.username: "Username пользователя",
        User.first_name: "Имя пользователя",
        User.last_name: "Фамилия пользователя",
        User.is_premium: "Премиум аккаунт",
        User.is_admin: "Администратор",
        User.is_banned: "Аккаунт забанен",
        User.created_at: "Дата регистрации пользователя",
        "cars_count": "Количество машин пользователя",
        "cars": "Машины пользователя"
    }
    column_details_list = (User.id,
                           User.username,
                           User.first_name,
                           User.last_name,
                           User.is_admin,
                           User.is_premium,
                           User.is_banned,
                           User.created_at,
                           "cars_count",
                           "cars")
    column_formatters = {
        User.created_at: lambda m, a: m.created_at.strftime("%d.%m.%Y %H:%M"),
        "cars": lambda m, a: [c.name for c in m.count_car],
        "cars_count": lambda m, a: len(m.count_car) if m.count_car else 0
    }
    column_formatters_detail = {
        User.created_at: lambda m, a: m.created_at.strftime("%d.%m.%Y %H:%M"),
        "cars": lambda m, a: [c.name for c in m.count_car],
        "cars_count": lambda m, a: len(m.count_car) if m.count_car else 0
    }
