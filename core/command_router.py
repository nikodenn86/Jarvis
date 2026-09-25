from core.actions.time import get_time, get_date

from core.actions.apps import (
    open_telegram,
    close_telegram,
    open_steam,
    close_steam,
    open_explorer,
    close_explorer,
    open_calculator,
    close_calculator,
)

from core.actions.browser import (
    open_browser,
    open_google,
    open_youtube,
)

from core.actions.system import (
    lock_computer,
    shutdown,
    restart,
)


class CommandRouter:
    def __init__(self):
        self.commands = [

            # Время и дата
            (
                [
                    "который час",
                    "сколько времени",
                    "сколько сейчас времени",
                ],
                get_time,
            ),

            (
                [
                    "какая сегодня дата",
                    "какое сегодня число",
                    "сегодняшняя дата",
                ],
                get_date,
            ),

            # Telegram
            (
                [
                    "открой telegram",
                    "открой телеграм",
                ],
                open_telegram,
            ),

            (
                [
                    "закрой telegram",
                    "закрой телеграм",
                ],
                close_telegram,
            ),

            # Steam
            (
                [
                    "открой steam",
                    "запусти steam",
                ],
                open_steam,
            ),

            (
                [
                    "закрой steam",
                    "закрой стим",
                ],
                close_steam,
            ),

            # Проводник
            (
                [
                    "открой проводник",
                    "открой файлы",
                ],
                open_explorer,
            ),

            (
                [
                    "закрой проводник",
                ],
                close_explorer,
            ),

            # Калькулятор
            (
                [
                    "открой калькулятор",
                    "запусти калькулятор",
                ],
                open_calculator,
            ),

            (
                [
                    "закрой калькулятор",
                ],
                close_calculator,
            ),

            # Браузер
            (
                [
                    "открой браузер",
                    "запусти браузер",
                ],
                open_browser,
            ),

            (
                [
                    "открой google",
                ],
                open_google,
            ),

            (
                [
                    "открой youtube",
                    "открой ютуб",
                ],
                open_youtube,
            ),

            # Система
            (
                [
                    "заблокируй компьютер",
                ],
                lock_computer,
            ),

            (
                [
                    "выключи компьютер",
                    "выключи пк",
                ],
                shutdown,
            ),

            (
                [
                    "перезагрузи компьютер",
                    "перезагрузи пк",
                ],
                restart,
            ),
        ]

    def route(self, text):
        text = text.lower().strip()

        for phrases, action in self.commands:
            for phrase in phrases:
                if phrase in text:
                    return action()

        return False, None