from nicegui import ui

from pages.dashboard import dashboard

ui.dark_mode().enable()

dashboard()

ui.run(
    title="Content Farm",
    port=8080,
    reload=True
)