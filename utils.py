from datetime import datetime
from pathlib import Path
from create_podcast import combine_mp3_files
def get_conversation_file():
    return open(Path(__file__).parent / f'conversations/conversation_{datetime.now().isoformat(sep="-", timespec="seconds")}.txt', 'a+', encoding='UTF-8')

def get_audio_file_path():
    return Path(__file__).parent / f'audios/audio_{datetime.now().isoformat(sep="-", timespec="seconds")}.mp3'

def summary(f, ai_client):
    f.flush()
    f.seek(0)
    text = f.read()
    print(text)
    #return text
    return ai_client.get_summary_response(text)

def finishPodcast(f, ai_client):
    summary_response = summary(f, ai_client)
    f.write("\nSummary:\n" + summary_response)
    #assemble
    # Example usage:
    input_folder = Path(__file__).parent / 'audios'
    start_file = Path(__file__).parent / 'static/start.mp3'
    end_file = Path(__file__).parent / 'static/end.mp3'
    output_file = Path(__file__).parent / f'result/result{datetime.now().isoformat(sep="-", timespec="seconds")}.mp3'
    combine_mp3_files(input_folder, start_file, end_file, output_file)