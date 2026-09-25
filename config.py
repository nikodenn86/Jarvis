import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3.8-flash"

VOSK_MODEL_PATH = "models/vosk"
VOSK_SAMPLE_RATE = 16000

WAKE_WORD = "джарвис"

LANGUAGE = "ru"

TTS_RATE = 175
TTS_VOLUME = 1.0