import flet as ft
def main(page: ft.Page):
    title=ft.Text(value="My first program", size=30)

    def button_clicked():
        print("Button clicked")
        page.add(ft.Text(value="Button clicked"))

    button = ft.Button(content=ft.Text(value="Click me"), on_click=button_clicked)
    row1=ft.Row(
        controls=[title,button]
    )
    radio=ft.RadioGroup(
        content=ft.Row(
        controls=[ft.Radio(label=f"{i}") for i in range(1, 4)],
        alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.add(title, button)
    page.add(row1)
    page.add(radio)
ft.run(main)