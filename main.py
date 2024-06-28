import flet as ft
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

#customize first question and the role
question = 'How do comparisons work in Python?'
role = 'You are a professional Python teacher.'

client = OpenAI()

isAsking = False

def main(page: ft.Page):
    messages = []
    tf = ft.TextField(value=question, expand=True, 
                      autofocus=True, shift_enter=True,
                      bgcolor=ft.colors.GREY_700,icon=ft.icons.WECHAT_OUTLINED)
    lf = ft.ListView(controls=messages, auto_scroll=False, expand=True, reverse=True)
    btt = ft.IconButton(icon=ft.icons.SEND_OUTLINED)

    def getMD(mdtxt):
        return  ft.Markdown(
            mdtxt,
            selectable=True,
            code_theme="atom-one-dark",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,

            on_tap_link=lambda e: page.launch_url(e.data),
        )
    
    def ask(e):
        global isAsking
        if isAsking:
            return
        isAsking = True
        btt.disabled = True
        responseText = ''
    
        question = tf.value
        mdQuestion =  getMD(question)

        messages.insert(0,ft.Card(
            content=ft.Container(padding=5,content=mdQuestion), 
            color=ft.colors.BLUE_400, margin=ft.Margin(left=10,right=0, top=5, bottom=5)))
        mdTxt = getMD(responseText)
        
        messages.insert(0,ft.Card(
            content=ft.Container(padding=5,content=mdTxt),
            color=ft.colors.GREY_700, margin=ft.Margin(left=0,right=10, top=5, bottom=5)))
        if len(messages) >= 100:    
            del messages[-2:] #if it is too long
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
                mdTxt.value = responseText
                #txt.value = responseText
                lf.scroll_to(0.0, duration=500)
                page.update()
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
