from pathlib import Path


VIDEO_EXT = (
    ".mp4",
    ".mov",
    ".mkv",
    ".avi",
    ".webm"
)


def scan_video(folder="videos"):

    folder = Path(folder)

    if not folder.exists():
        return []

    videos = []

    for file in folder.iterdir():

        if file.suffix.lower() in VIDEO_EXT:

            videos.append(file)

    return videos