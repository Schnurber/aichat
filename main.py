import flet as ft
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

#customize first question and the role
question = 'Wer bist Du?'
role = 'Du führst eine Unterhaltung und gibst eine kurze Antwort. Der letzte Satz ist immer eine Frage'
speech_file_path = Path(__file__).parent / "speech.mp3"
MAX_ROUNDS = 100

numRounds = 0
client1 = OpenAI()
client2 = OpenAI()
client = client1

isAsking = False
isPlaying = False

def main(page: ft.Page):
    messages = []
    tf = ft.TextField(value=question, expand=True, 
                      autofocus=True, shift_enter=True,
                      bgcolor=ft.colors.GREY_700,icon=ft.icons.WECHAT_OUTLINED)
    lf = ft.ListView(controls=messages, auto_scroll=False, expand=True, reverse=True)
    btt = ft.IconButton(icon=ft.icons.PLAY_ARROW)
    btt_stop = ft.IconButton(icon=ft.icons.STOP)
    btt_stop.disabled = True

    def getCard(txt, ab):
        if ab:
            return ft.Card(
                content=ft.Container(padding=5,content=txt), 
                color=ft.colors.BLUE_400, margin=ft.Margin(left=10,right=0, top=5, bottom=5))
        else:
            return ft.Card(
                content=ft.Container(padding=5,content=txt),
                color=ft.colors.GREY_700, margin=ft.Margin(left=0,right=10, top=5, bottom=5))
        
    def ask(e):
        global isAsking, numRounds, MAX_ROUNDS, client, isPlaying
        question = tf.value
        numRounds = 0
        if isAsking or question == '':
            return
        
        isAsking = True
        btt.disabled = True
        btt_stop.disabled = False
        quest = ft.Text(question, selectable=True)
        messages.insert(0,getCard(quest,True))
        
        while numRounds < MAX_ROUNDS:
            numRounds += 1
            responseText = ''
            tf.value = ''
            
            txt = ft.Text(responseText, selectable=True)
            messages.insert(0,getCard(txt, client == client2))
            if len(messages) >= 100:    
                del messages[-2:] #if it is too long
            
            try:
                stream = client.chat.completions.create(
                    model="gpt-4-turbo",
                    stream=True,
                    messages=[
                        {"role": "system", "content": role},
                        {"role": "user", "content": question}
                    ]
                )
                for chunk in stream:
                    msg = chunk.choices[0].delta
                    if msg.content is not None:
                        responseText += msg.content
                        txt.value = responseText
                        lf.scroll_to(0.0, duration=500)
                        page.update()
            except:
                txt.value = ' NO INTERNET CONNECTION!'
                lf.scroll_to(0.0, duration=500)

            with client.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice="alloy" if client==client1 else "onyx",
                input=responseText,
            ) as response:
                response.stream_to_file(speech_file_path)
                while (not response.is_closed):
                    pass

            audio1 = ft.Audio( src=speech_file_path, autoplay=True)
            page.overlay.append(audio1)
            isPlaying = True
            def ply(e):
                global isPlaying
                if e.data == 'completed':
                    isPlaying = False
                    
            audio1.on_state_changed = ply
            while isPlaying:
                page.update()
            #remove last audio    
            page.overlay.pop()
            question = responseText

            if client == client1:
                client = client2
            else:
                client = client1


        btt.disabled = False
        btt_stop.disabled = True
        page.update()
        client = client1
        isAsking = False

    def stop(e):
        global numRounds
        numRounds = MAX_ROUNDS
        btt_stop.disabled = True

    btt.on_click = ask
    tf.on_submit = ask
    btt_stop.on_click=stop

    container= ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
            lf,
            ft.Row(
                controls=[
                tf,
                btt, btt_stop
            ])
        ])
    )

    page.add(container)
    
ft.app(main)
