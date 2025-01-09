import flet as ft

def create_text_field(on_submit, initial_value):
    return ft.TextField(
        value=initial_value,
        expand=True,
        autofocus=True,
        shift_enter=True,
        bgcolor=ft.colors.GREY_700,
        icon=ft.icons.WECHAT_OUTLINED,
        on_submit=on_submit
    )

def create_list_view(messages):
    return ft.ListView(controls=messages, auto_scroll=False, expand=True, reverse=True)

def create_icon_buttons(on_ask_click, on_stop_click):
    btt = ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=on_ask_click)
    btt_stop = ft.IconButton(icon=ft.icons.STOP, disabled=True, on_click=on_stop_click)
    return btt, btt_stop

def create_card(txt, ab):
    color = ft.colors.GREY_700 if ab else ft.colors.BLUE_400
    margin = ft.Margin(left=0, right=10, top=5, bottom=5) if ab else ft.Margin(left=10, right=0, top=5, bottom=5)
    return ft.Card(
        content=ft.Container(padding=5, content=txt),
        color=color,
        margin=margin
    )