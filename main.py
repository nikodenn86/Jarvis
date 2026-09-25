from core.stt import SpeechRecognizer
from core.assistant import JarvisAssistant
from core.command_router import CommandRouter

from voice.tts import JarvisVoice
from ai.gemini import GeminiBrain


def main():

    print()
    print(
        "======================================"
    )
    print(
        "             JARVIS 2.0"
    )
    print(
        "======================================"
    )
    print()

    # STT

    speech = SpeechRecognizer()

    # Голос

    voice = JarvisVoice()

    # Локальные команды

    router = CommandRouter()

    # Gemini

    brain = GeminiBrain()

    # Ассистент

    assistant = JarvisAssistant(
        speech=speech,
        voice=voice,
        router=router,
        brain=brain
    )

    # Запуск

    assistant.run()


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print()
        print(
            "Jarvis остановлен."
        )

    except Exception as error:

        print()
        print(
            f"[CRITICAL ERROR] {error}"
        )