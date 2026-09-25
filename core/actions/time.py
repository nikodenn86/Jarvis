from datetime import datetime


def get_time():

    current_time = datetime.now().strftime(
        "%H:%M"
    )

    return (
        True,
        f"Сейчас {current_time}, сэр."
    )


def get_date():

    current_date = datetime.now().strftime(
        "%d.%m.%Y"
    )

    return (
        True,
        f"Сегодня {current_date}, сэр."
    )