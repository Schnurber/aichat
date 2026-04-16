import flet as ft
from openai import OpenAI
from dotenv import load_dotenv
import asyncio
load_dotenv()

#customize first question and the role
question = 'Wer war Ada Lovelace?'
role = 'Du bist Johann Wolfgang von Goethe, der berühmte deutsche Dichter und Denker. Beantworte die folgende Frage in deinem charakteristischen Stil: ' + question

client = OpenAI()

isAsking = False


async def speak_text(text: str):
    if not text:
        return
    try:
        # Startet den macOS Sprachaufruf als Terminal-Prozess.
        process = await asyncio.create_subprocess_exec("say", text)
        await process.wait()
    except Exception:
        # Audioausgabe ist optional und darf den Chatfluss nicht unterbrechen.
        pass

def main(page: ft.Page):
    messages = []
    tf = ft.TextField(value=question, expand=True, 
                      autofocus=True, shift_enter=True,
                      bgcolor=ft.Colors.GREY_700,icon=ft.Icons.WECHAT_OUTLINED)
    lf = ft.ListView(controls=messages, auto_scroll=False, expand=True, reverse=True)
    btt = ft.IconButton(icon=ft.Icons.SEND_OUTLINED)
    
    async def ask(e):
        global isAsking
        question = tf.value
        if isAsking or question == '':
            return
        isAsking = True
        btt.disabled = True
        responseText = ''
    
        tf.value = ''

        messages.insert(0,ft.Card(
            content=ft.Container(padding=5,content=ft.Text(question, selectable=True)), 
            bgcolor=ft.Colors.BLUE_400, margin=ft.Margin(left=10,right=0, top=5, bottom=5)))
        
        txt = ft.Text(responseText, selectable=True)
        messages.insert(0,ft.Card(
            content=ft.Container(padding=5,content=txt),
            bgcolor=ft.Colors.GREY_700, margin=ft.Margin(left=0,right=10, top=5, bottom=5)))
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
                    await lf.scroll_to(0.0, duration=500)
                    page.update()
        except:
            txt.value = ' NO INTERNET CONNECTION!'
            await lf.scroll_to(0.0, duration=500)
        # Antwort als Audio über macOS "say" ausgeben.
        await speak_text(responseText)
        
        btt.disabled = False
        page.update()
        isAsking = False

    btt.on_click = ask
    tf.on_submit = ask
    container= ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
            lf,
            ft.Row(
                controls=[
                tf,
                btt
            ])
        ])
    )

    page.add(container)
    
ft.run(main)
