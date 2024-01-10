import flet as ft 

def main(page: ft.page):
    page.title = "Flet Counter App"
    page.theme_mode = "light"
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)