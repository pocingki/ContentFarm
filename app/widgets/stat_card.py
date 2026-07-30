from nicegui import ui


class StatCard:

    def __init__(self, title, value, color='blue'):

        with ui.card().classes('w-60 p-4'):

            ui.label(title).classes('text-lg')

            self.value = ui.label(str(value)).classes(
                f'text-5xl text-{color}-600 font-bold'
            )

    def set(self, value):

        self.value.set_text(str(value))