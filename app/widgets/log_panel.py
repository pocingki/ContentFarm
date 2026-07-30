from nicegui import ui


class LogPanel:

    def __init__(self):

        self.logs = ui.log(max_lines=300).classes('w-full h-72')

    def write(self, text):

        self.logs.push(text)