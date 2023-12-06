import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    input = ft.TextField(label="Entrada",width=200)
    answer = ft.Text('')
    def plus_click(e):
        input.value = str('')
        answer.value = 'We receive your input!!!'
        page.update()


    btn = ft.ElevatedButton("Click me!",on_click=plus_click)
    
    page.add(input,btn,answer)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)