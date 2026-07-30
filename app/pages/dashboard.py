from nicegui import ui

from widgets.stat_card import StatCard
from widgets.log_panel import LogPanel

from services.scanner import scan_video
from services.excel_reader import read_excel


def dashboard():

    # ===== Judul =====
    ui.label(
        '🚀 CONTENT FARM'
    ).classes('text-3xl font-bold')

    ui.separator()

    # ===== Statistik =====
    with ui.row():

        total_video = StatCard(
            '📹 Video',
            0,
            'blue'
        )

        queue = StatCard(
            '📅 Queue',
            0,
            'orange'
        )

        uploaded = StatCard(
            '✅ Uploaded',
            0,
            'green'
        )

    ui.separator()

    # ===== Tombol =====
    with ui.row():

        scan_button = ui.button(
            '📂 Scan Folder'
        )

        excel_button = ui.button(
            '📄 Read Excel'
        )

    ui.separator()

    # ===== Log =====
    log = LogPanel()

    ui.separator()

    # ===== Table =====
    table = ui.table(
        columns=[],
        rows=[]
    ).classes('w-full')

    # ===================================================
    # Scan Folder
    # ===================================================

    def scan():

        videos = scan_video()

        total_video.set(len(videos))

        log.write(
            f'📂 Scan selesai. {len(videos)} video ditemukan.'
        )

        for video in videos:

            log.write(video.name)

    # ===================================================
    # Read Excel
    # ===================================================

    def load_excel():

        df = read_excel()

        if df is None:

            log.write(
                '❌ Excel tidak ditemukan.'
            )

            return

        table.columns = [
            {
                "name": c,
                "label": c,
                "field": c
            }

            for c in df.columns
        ]

        table.rows = df.to_dict("records")

        table.update()

        queue.set(len(df))

        log.write(
            f'📄 Excel berhasil dibaca ({len(df)} data).'
        )

    # ===== Event Button =====

    scan_button.on_click(scan)

    excel_button.on_click(load_excel)