# Importing flet as ft object
import flet as ft

# Function main() is an empty entry point in a Flet application
# Page is like a "canvas" specific to a user, a visual state of a user session.
# To build an application UI you add and remove controls to a page, update their properties.


def main(page: ft.Page):
    pass

# By Default flet app starts in a native OS window


ft.app(target=main)

# Displaying flet in Web Browser
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
