import time

import flet as ft


def main(page: ft.Page):
    t = ft.Text()
    button = ft.ElevatedButton(text="Oh no")

    def button_clicked(e):
        for i in range(10):
            page.add(t)
            t.value = f"{i}"
            page.update()
            time.sleep(0.5)

    page.add(ft.Text("Hello"))
    page.add(ft.ElevatedButton(text="Click Me", on_click=button_clicked))


ft.app(target=main)
