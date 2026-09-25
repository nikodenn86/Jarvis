import subprocess


def lock_computer():

    subprocess.run(
        [
            "rundll32.exe",
            "user32.dll,LockWorkStation"
        ]
    )

    return (
        True,
        "Компьютер заблокирован, сэр."
    )


def shutdown():

    subprocess.run(
        [
            "shutdown",
            "/s",
            "/t",
            "10"
        ]
    )

    return (
        True,
        "Компьютер будет выключен через десять секунд, сэр."
    )


def restart():

    subprocess.run(
        [
            "shutdown",
            "/r",
            "/t",
            "10"
        ]
    )

    return (
        True,
        "Компьютер будет перезагружен через десять секунд, сэр."
    )