# sudo apt install libmpv1
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение на Flet"    
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")

    greeting_history = []

    history_column = ft.Column(visible=True)
    show_history = True 

    def update_history_view():
        history_controls = [ft.Text("История приветствий:", size='bodyMedium')]
        for ind, name in enumerate(greeting_history):
            history_controls.append(
                ft.Row([
                    ft.Text(name),
                    ft.IconButton(icon=ft.Icons.CLOSE, tooltip='Удалить',
                                  on_click=lambda e, i=ind: remove_name_from_history(i))
                ])
            )
        history_column.controls = history_controls
        page.update()

    def remove_name_from_history(index):
        if 0 <= index < len(greeting_history):  
            del greeting_history[index]
            update_history_view()

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
            name_input.value = ""
            greeting_history.append(name)
            update_history_view()
        else:
            greeting_text.value = "Пожалуйста, введите имя."
        
        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def clear_history(_):
        greeting_history.clear()
        update_history_view()

    def copy_greeting(_):
        page.set_clipboard(greeting_text.value)

    def toggle_history(_):
        nonlocal show_history
        show_history = not show_history
        history_column.visible = show_history
        toggle_history_button.icon = ft.Icons.VISIBILITY if not show_history else ft.Icons.VISIBILITY_OFF
        toggle_history_button.tooltip = "Показать историю" if not show_history else "Скрыть историю"
        page.update()

    name_input = ft.TextField(label="Введите ваше имя", autofocus=True, on_submit=on_button_click)

    clear_button = ft.ElevatedButton("Очистить историю", icon=ft.Icons.DELETE, on_click=clear_history)
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, tooltip='Сменить тему', on_click=toggle_theme)
    greet_button = ft.ElevatedButton("Поздороваться", icon=ft.Icons.HANDSHAKE, on_click=on_button_click)
    copy_button = ft.IconButton(icon=ft.Icons.COPY, tooltip='Скопировать приветствие', on_click=copy_greeting)
    toggle_history_button = ft.IconButton(icon=ft.Icons.VISIBILITY_OFF, tooltip="Скрыть историю", on_click=toggle_history)

    update_history_view()

    page.add(
        ft.Row([greeting_text, copy_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([name_input, greet_button, theme_button, clear_button, toggle_history_button], alignment=ft.MainAxisAlignment.CENTER),
        history_column
    )

ft.app(main, view=ft.WEB_BROWSER)