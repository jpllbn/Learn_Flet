# You can modify control properties and the UI will be updated on the next page.
# update():
import time

import flet as ft


def main(page: ft.Page):
    t = ft.Text()
    page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(1, 11):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)


ft.app(target=main)
