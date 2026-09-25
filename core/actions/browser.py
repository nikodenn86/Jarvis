import webbrowser


def open_browser():

    webbrowser.open(
        "https://www.google.com"
    )

    return (
        True,
        "Открываю браузер, сэр."
    )


def open_google():

    webbrowser.open(
        "https://www.google.com"
    )

    return (
        True,
        "Открываю Google, сэр."
    )


def open_youtube():

    webbrowser.open(
        "https://www.youtube.com"
    )

    return (
        True,
        "Открываю YouTube, сэр."
    )