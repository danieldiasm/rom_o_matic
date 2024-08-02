# ROM Download Class

# TODO Documentation
# TODO Docstrings
# TODO Logging
# TODO Tests

import hashlib
import downloader.url_extractor as url_extractor
import downloader.data_extractor as data_extractor

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
        extractor = url_extractor.Page(page_url= self.rom_page_url)
        self.bs4_page = extractor.get_bs4_page()
        self.download_url = extractor.extract_download_url()


    def extract_game_data(self):
        self.game_data = data_extractor.GameData.extract(self.bs4_page)


    def download_rom(self):
        # TODO This should be worked on another branch
        pass


    def make_hash(self):
        hash_obj = hashlib.md5(bytes(self.rom_page_url, 'utf-8'))
        self.id = str(hash_obj.hexdigest())


    def set_download_state(self, status: bool) -> bool:
        self.download_status = status
        return self.download_status


    def get_download_state(self):
        return self.download_status


    def get_download_url(self) -> str:
        return self.download_url


    def get_download_title(self) -> str:
        return self.title


    def get_download_id(self) -> str:
        return self.id
