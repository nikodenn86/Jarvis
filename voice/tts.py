import pyttsx3

from config import TTS_RATE, TTS_VOLUME


class JarvisVoice:

    def __init__(self):

        print("[TTS] Инициализация голоса...")

        self.engine = pyttsx3.init()

        self.engine.setProperty(
            "rate",
            TTS_RATE
        )

        self.engine.setProperty(
            "volume",
            TTS_VOLUME
        )

        self._select_russian_voice()

        print("[TTS] Голос готов.")

    def _select_russian_voice(self):

        voices = self.engine.getProperty("voices")

        print("[TTS] Доступные голоса:")

        for voice in voices:

            print(
                f"  - {voice.name} | {voice.id}"
            )

            voice_info = (
                f"{voice.name} "
                f"{voice.id}"
            ).lower()

            if (
                "russian" in voice_info
                or "ru-" in voice_info
                or "рус" in voice_info
            ):

                self.engine.setProperty(
                    "voice",
                    voice.id
                )

                print(
                    f"[TTS] Выбран голос: "
                    f"{voice.name}"
                )

                return

        print(
            "[TTS] Русский голос "
            "автоматически не найден."
        )

    def speak(self, text):

        if not text:
            return

        print(f"[JARVIS] {text}")

        self.engine.say(text)
        self.engine.runAndWait()