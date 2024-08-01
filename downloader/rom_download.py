# ROM Download Class

class ROM:

    def __init__(self, title, rom_page_url, download_path) -> None:
        self.title = title
        self.rom_page_url = rom_page_url
        self.download_url = None
        self.download_status = False
        self.download_path = download_path
        self.bs4_page = None
        self.game_data = {}
