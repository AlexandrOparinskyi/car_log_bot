from datetime import datetime, date


def get_current_date(created_date: datetime) -> str:
    """
    Вычисляет период работы с ботом и возвращает
    строку с правильным склонением

    :param created_date: дата создания пользователя
    :return: строчку с периодом работы
    """
    today = date.today()

    if isinstance(created_date, datetime):
        created_date = created_date.date()

    years = today.year - created_date.year
    months = today.month - created_date.month
    days = today.day - created_date.day

    if days < 0:
        months -= 1
        if today.month == 1:
            last_month = date(today.year - 1, 12, 1)
        else:
            last_month = date(today.year, today.month - 1, 1)
        days_in_prev_month = (date(last_month.year, last_month.month + 1, 1) -
                              date(last_month.year, last_month.month, 1)).days
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

        # Функции для склонения слов

    def plural_days(n):
        if n % 10 == 1 and n % 100 != 11:
            return 'день'
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            return 'дня'
        else:
            return 'дней'

    def plural_months(n):
        if n % 10 == 1 and n % 100 != 11:
            return 'месяц'
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            return 'месяца'
        else:
            return 'месяцев'

    def plural_years(n):
        if n % 10 == 1 and n % 100 != 11:
            return 'год'
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            return 'года'
        else:
            return 'лет'

        # Формируем результат

    result_parts = []

    if years > 0:
        result_parts.append(f"{years} {plural_years(years)}")

    if months > 0:
        result_parts.append(f"{months} {plural_months(months)}")

    if days > 0:
        result_parts.append(f"{days} {plural_days(days)}")

    # Если пользователь создан сегодня
    if not result_parts:
        return "менее дня"

    return " ".join(result_parts)


def plural_records(n):
    """
    Правильно склоняет слово 'запись' в зависимости от числа

    Args:
        n: количество записей (int)

    Returns:
        str: правильная форма слова
    """
    if n % 10 == 1 and n % 100 != 11:
        return f'{n} запись'
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return f'{n} записи'
    else:
        return f'{n} записей'
