import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent 

def main(page: ft.page):
    page.title = "Flet Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "light"
    text_number: TextField = TextField(value="0", text_align=ft.TextAlign.RIGHT, width=80)

    def dec_count(e: ControlEvent) -> None:
        text_number.value = f"{int(text_number.value) - 1}"
        page.update()
    
    def inc_count(e: ControlEvent) -> None:
        text_number.value = f"{int(text_number.value) + 1}"
        page.update()
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=dec_count),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=inc_count)
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)