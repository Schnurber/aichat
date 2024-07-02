import flet as ft
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

#customize first question and the role
question = 'Who was Ada Lovelace?'
role = 'You are William Shakespeare and you only speak in rhyme.'

client = OpenAI()

isAsking = False

def main(page: ft.Page):
    messages = []
    tf = ft.TextField(value=question, expand=True, 
                      autofocus=True, shift_enter=True,
                      bgcolor=ft.colors.GREY_700,icon=ft.icons.WECHAT_OUTLINED)
    lf = ft.ListView(controls=messages, auto_scroll=False, expand=True, reverse=True)
    btt = ft.IconButton(icon=ft.icons.SEND_OUTLINED)
    
    def ask(e):
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
            color=ft.colors.BLUE_400, margin=ft.Margin(left=10,right=0, top=5, bottom=5)))
        
        txt = ft.Text(responseText, selectable=True)
        messages.insert(0,ft.Card(
            content=ft.Container(padding=5,content=txt),
            color=ft.colors.GREY_700, margin=ft.Margin(left=0,right=10, top=5, bottom=5)))
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
    
ft.app(main)
