# Controls
# User interface is made of Controls (aka widgets).
# To make controls visible to a user they must be added to a Page or inside other controls.
# Page is the top-most control. Nesting controls into each other could be represented as a tree with Page as a root.
# Controls are just regular Python classes.
# Create control instances via constructors with parameters matching their properties

import flet as ft


def main(page: ft.Page):
    hello = ft.Text(value="Hello World", color="orange")
    page.controls.append(hello)
    page.update()


ft.app(target=main)
