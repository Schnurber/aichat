import flet as ft
from config import conf
from ai_client import AIClient
from ui_components import create_text_field, create_list_view, create_icon_buttons, create_card
from utils import get_conversation_file, get_audio_file_path, finishPodcast, summary
import random

MAX_ROUNDS = 30

def main(page: ft.Page):
    messages = []
    ai_client = AIClient()

    def stop(e):
        global numRounds
        numRounds = MAX_ROUNDS
        btt_stop.disabled = True



    def ask(e):
        global isAsking, numRounds, isPlaying
        numRounds = 0
        with get_conversation_file() as f:
            question = tf.value.strip()
            if isAsking or not question:
                return

            isAsking = True
            btt.disabled = True
            btt_stop.disabled = False
            quest = ft.Text(question, selectable=True)
            messages.insert(0, create_card(quest, False))
            f.write(f'{question}\n')
            responseText = question
            
            while numRounds < MAX_ROUNDS:
                numRounds += 1
                tf.value = ''
                
                if numRounds > 1:
                    responseText = ''
                    txt = ft.Text(responseText, selectable=True)
                    messages.insert(0, create_card(txt, ai_client.current == ai_client.specialist))
                    if len(messages) >= 100:    
                        del messages[-2:]
                    
                    try:
                        summa = summary(f, ai_client)
                        stream = ai_client.get_stream_response(question, conf['moderator']['role'] + random.choice([" Der letzte Satz ist eine Frage. ",""]) if ai_client.current == ai_client.moderator else conf['specialist']['role'], summa)
                        for chunk in stream:
                            msg = chunk.choices[0].delta
                            if msg.content:
                                responseText += msg.content
                                f.write(msg.content)
                                txt.value = responseText
                                lf.scroll_to(0.0, duration=500)
                                page.update()
                        f.write('\n')
                    except Exception:
                        txt.value = ' NO INTERNET CONNECTION!'
                        lf.scroll_to(0.0, duration=500)
                
                speech_file_path = get_audio_file_path()
                with ai_client.current.audio.speech.with_streaming_response.create(
                    model="tts-1",
                    voice="alloy" if ai_client.current == ai_client.moderator else "onyx",
                    input=responseText,
                ) as response:
                    response.stream_to_file(speech_file_path)
                    while not response.is_closed:
                        pass
                
                audio1 = ft.Audio(src=speech_file_path, autoplay=True)
                page.overlay.append(audio1)
                isPlaying = True

                def ply(e):
                    global isPlaying
                    if e.data == 'completed':
                        isPlaying = False
                    
                audio1.on_state_changed = ply
                page.update()

                while isPlaying:
                    page.update()
                
                page.overlay.pop()
                question = responseText

                ai_client.switch_client()

            finishPodcast(f, ai_client)
            btt.disabled = False
            btt_stop.disabled = True
            page.update()
            ai_client.current = ai_client.moderator
            isAsking = False

    tf = create_text_field(on_submit=ask, initial_value=conf['moderator']['first_question'])
    lf = create_list_view(messages)
    btt, btt_stop = create_icon_buttons(on_ask_click=ask, on_stop_click=stop)

    global isAsking, numRounds, isPlaying
    isAsking = False
    isPlaying = False

    container = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                lf,
                ft.Row(
                    controls=[tf, btt, btt_stop]
                )
            ]
        )
    )

    page.add(container)

ft.app(main)