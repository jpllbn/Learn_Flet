# Some controls are "container" controls (like Page) which could contain other controls.
# For example,
# Row control allows arranging other controls in a row one-by-one:


import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C"),

            # or TextField and ElevatedButton next to it
            ft.TextField(label="You Name"),
            ft.ElevatedButton(text="Say my name")
        ]
        )
    )


ft.app(target=main)
