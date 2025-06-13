# tasks/transcription.py
import whisper

# carica il modello "base" (220 MB approx) — zero registrazione
_model = whisper.load_model("base")

def transcribe(audio_path: str, language: str = "en") -> str:
    result = _model.transcribe(audio_path, language=language)
    return result["text"]
