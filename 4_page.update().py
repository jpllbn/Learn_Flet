# page.update() is smart enough to send only the changes made since its last call,
# so you can add a couple of new controls to the page, remove some of them,
# change other controls' properties and then call page.update() to do a batched update
import time

import flet as ft


def main(page: ft.Page):
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)


ft.app(target=main)