from datetime import datetime
from pathlib import Path

def get_conversation_file():
    return open(f'conversations/conversation_{datetime.now().isoformat(sep="-", timespec="seconds")}.txt', 'a+', encoding='UTF-8')

def get_audio_file_path():
    return Path(__file__).parent / f'audios/audio_{datetime.now().isoformat(sep="-", timespec="seconds")}.mp3'