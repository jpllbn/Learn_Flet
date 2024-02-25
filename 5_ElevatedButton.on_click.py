import flet as ft


def main(page: ft.Page):
    def button_click(e):
        page.add(ft.Text("Clicked"))

    button = ft.ElevatedButton(text="Click Me", on_click=button_click)
    page.add(button)


ft.app(target=main)
