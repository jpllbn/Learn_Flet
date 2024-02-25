import flet as ft


def main(page: ft.Page):
    def add_clicked(e):
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's need to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("add", on_click=add_clicked)]))


ft.app(target=main)
