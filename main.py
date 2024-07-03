import flet as ft
from gpt4all import GPT4All
#customize first question and the role

client = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

#question = 'Who was Ada Lovelace?'
#role = 'You are William Shakespeare and you only speak in rhyme.'
# works also in German
question = 'Wer war Ada Lovelace?'
role = 'Du bist Johann Wolfgang von Goethe und sprichst nur in Reimen.'

# use other files from huggingface:
# Download: 
# https://huggingface.co/TheBloke/em_german_leo_mistral-GGUF/blob/main/em_german_leo_mistral.Q2_K.gguf
# client = GPT4All(model_name="em_german_leo_mistral.Q2_K.gguf", model_path='../../Downloads')
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
            stream = client.generate(
                streaming=True,
                prompt=role + ' ' + question + '', # modify for other prompt template
            )
            for chunk in stream:
                if chunk is not None:
                    responseText += chunk if chunk != ' \n' else ''
                    txt.value = responseText
                    lf.scroll_to(0.0, duration=500)
                    page.update()
        except Exception as e:
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
