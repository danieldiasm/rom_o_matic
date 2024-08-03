# ROM Listing main file
# ROM Download Class

# TODO Documentation
# TODO Docstrings
# TODO Logging
# TODO Tests

import hashlib
import cool_rom.url_extractor as url_extractor
import cool_rom.data_extractor as data_extractor

class Console_Listing:

    def __init__(self, rom_page_url) -> None:
        self.console_listing_page_url = rom_page_url
        self.bs4_page = None
        self.consoles_url_list = []

# Particular Methods

    def extract_console_listing_url(self):
        # self.game_data = data_extractor.GameData.extract(self.bs4_page)
        pass

    def make_hash(self):
        hash_obj = hashlib.md5(bytes(self.rom_page_url, 'utf-8'))
        self.id = str(hash_obj.hexdigest())

# Getters

    def get_consoles_url_list(self):
        return self.consoles_url_list

