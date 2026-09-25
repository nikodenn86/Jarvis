import json
import queue

import sounddevice as sd
from vosk import Model, KaldiRecognizer

from config import VOSK_MODEL_PATH, VOSK_SAMPLE_RATE


class SpeechRecognizer:

    def __init__(self):

        print("[STT] Загрузка модели Vosk...")

        self.audio_queue = queue.Queue()

        self.model = Model(VOSK_MODEL_PATH)

        self.recognizer = KaldiRecognizer(
            self.model,
            VOSK_SAMPLE_RATE
        )

        print("[STT] Vosk готов.")

    def _callback(
        self,
        indata,
        frames,
        time_info,
        status
    ):

        if status:
            print(f"[STT] {status}")

        self.audio_queue.put(
            bytes(indata)
        )

    def listen(self):

        print("[STT] Слушаю...")

        with sd.RawInputStream(
            samplerate=VOSK_SAMPLE_RATE,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self._callback
        ):

            while True:

                data = self.audio_queue.get()

                if self.recognizer.AcceptWaveform(data):

                    result = json.loads(
                        self.recognizer.Result()
                    )

                    text = result.get(
                        "text",
                        ""
                    ).strip()

                    if text:
                        yield text