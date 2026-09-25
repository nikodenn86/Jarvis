import os
import subprocess


# =========================
# TELEGRAM
# =========================

def open_telegram():
    try:
        os.startfile("tg://resolve")
        return True, "Открываю Telegram, сэр."
    except Exception:
        return False, "Не удалось открыть Telegram, сэр."


def close_telegram():
    result = subprocess.run(
        ["taskkill", "/IM", "Telegram.exe", "/F"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True, "Закрываю Telegram, сэр."

    return False, "Telegram сейчас не запущен, сэр."


# =========================
# STEAM
# =========================

def open_steam():
    try:
        os.startfile("steam://open/main")
        return True, "Запускаю Steam, сэр."
    except Exception:
        return False, "Не удалось открыть Steam, сэр."


def close_steam():
    result = subprocess.run(
        ["taskkill", "/IM", "steam.exe", "/F"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True, "Закрываю Steam, сэр."

    return False, "Steam сейчас не запущен, сэр."


# =========================
# Проводник
# =========================

def open_explorer():
    try:
        subprocess.Popen("explorer")
        return True, "Открываю проводник, сэр."
    except Exception:
        return False, "Не удалось открыть проводник, сэр."


def close_explorer():
    result = subprocess.run(
        ["taskkill", "/IM", "explorer.exe", "/F"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True, "Закрываю проводник, сэр."

    return False, "Проводник сейчас не запущен, сэр."


# =========================
# Калькулятор
# =========================

def open_calculator():
    try:
        subprocess.Popen("calc.exe")
        return True, "Калькулятор запущен, сэр."
    except Exception:
        return False, "Не удалось открыть калькулятор, сэр."


def close_calculator():
    result = subprocess.run(
        ["taskkill", "/IM", "CalculatorApp.exe", "/F"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True, "Закрываю калькулятор, сэр."

    return False, "Калькулятор сейчас не запущен, сэр."