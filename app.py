import flet as ft

def main(page: ft.Page):
    page.title = "Flet di Railway"
    page.add(ft.Text("Halo, ini aplikasi Flet di Railway!"))

ft.app(target=main, view=ft.WEB_BROWSER, port=8501)
