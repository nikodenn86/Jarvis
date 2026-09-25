from config import WAKE_WORD


class JarvisAssistant:

    def __init__(
        self,
        speech,
        voice,
        router,
        brain
    ):

        self.speech = speech
        self.voice = voice
        self.router = router
        self.brain = brain

        self.running = True

    def process_text(self, text):

        text = text.lower().strip()

        print(
            f"[USER] {text}"
        )

        # Проверяем wake word

        if WAKE_WORD not in text:

            return

        # Убираем "джарвис"

        command = text.replace(
            WAKE_WORD,
            "",
            1
        ).strip()

        # Просто "Джарвис"

        if not command:

            self.voice.speak(
                "Да, сэр?"
            )

            return

        # Выход

        if (
            command == "выход"
            or command == "завершение работы"
        ):

            self.voice.speak(
                "До свидания, сэр."
            )

            self.running = False

            return

        # Локальная команда

        handled, response = (
            self.router.route(command)
        )

        if handled:

            self.voice.speak(
                response
            )

            return

        # Gemini

        print(
            "[ROUTER] Передаю запрос Gemini..."
        )

        response = self.brain.ask(
            command
        )

        self.voice.speak(
            response
        )

    def run(self):

        print()
        print(
            "================================"
        )
        print(
            "       JARVIS ЗАПУЩЕН"
        )
        print(
            "================================"
        )
        print()
        print(
            "Скажите «Джарвис»..."
        )
        print()

        for text in self.speech.listen():

            if not self.running:
                break

            self.process_text(text)

        print(
            "\n[JARVIS] Работа завершена."
        )