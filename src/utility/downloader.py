from PySide6.QtCore import QThread, Signal
from urllib.request import urlopen
from pathlib import Path


class Downloader(QThread):
    got_total_progress = Signal(int)
    got_current_progress = Signal(int)
    succeeded = Signal()

    def __init__(self, url: str, file_path: Path):
        super().__init__()
        self.url = url
        self.file_path = file_path

    def run(self):
        saved_bytes = 0
        CHUNK_SIZE = 1024
        with urlopen(self.url) as req:
            self.got_total_progress.emit(int(req.info()["Content-Length"]))
            with open(self.file_path, "ab") as file:
                while True:
                    chunk = req.read(CHUNK_SIZE)
                    if chunk is None:
                        continue
                    elif chunk == b"":
                        break
                    file.write(chunk)
                    saved_bytes += CHUNK_SIZE
                    self.got_current_progress.emit(saved_bytes)
        self.succeeded.emit()
