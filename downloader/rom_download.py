# ROM Download Class

class ROM:

    def __init__(self, title, rom_page_url, download_path) -> None:
        self.id = None
        self.title = title
        self.rom_page_url = rom_page_url
        self.download_url = None
        self.download_status = False
        self.download_path = download_path
        self.bs4_page = None
        self.game_data = {}
    
    def extract_download_url(self):
        pass

    def extract_game_data(self):
        pass

    def download_rom(self):
        pass

    def make_hash(self):
        pass

    def set_download_state(self):
        pass

    def get_download_state(self):
        pass

    def get_download_url(self):
        pass

    def get_download_title(self):
        pass

    def get_download_id(self):
        pass
