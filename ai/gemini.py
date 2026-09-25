from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL
from ai.prompts import SYSTEM_PROMPT


class GeminiBrain:

    def __init__(self):

        if not GEMINI_API_KEY:
            raise RuntimeError(
                "Переменная GEMINI_API_KEY не установлена."
            )

        print("[AI] Подключение к Gemini...")

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.previous_interaction_id = None

        print(
            f"[AI] Модель: {GEMINI_MODEL}"
        )

        print("[AI] Gemini готов.")

    def ask(self, text):

        try:

            request = {
                "model": GEMINI_MODEL,
                "input": (
                    f"{SYSTEM_PROMPT}\n\n"
                    f"Пользователь: {text}"
                ),
                "generation_config": {
                    "thinking_level": "low"
                }
            }

            if self.previous_interaction_id:

                request[
                    "previous_interaction_id"
                ] = self.previous_interaction_id

            response = self.client.interactions.create(
                **request
            )

            self.previous_interaction_id = response.id

            answer = response.output_text

            if not answer:

                return (
                    "Сэр, Gemini не вернул ответ."
                )

            return answer.strip()

        except Exception as error:

            print(
                f"[AI ERROR] {error}"
            )

            return (
                "Сэр, сейчас я не могу "
                "получить ответ от Gemini."
            )