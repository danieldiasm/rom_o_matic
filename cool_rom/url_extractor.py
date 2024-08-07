# Download link exrtactor

# TODO Documentation
# TODO Docstrings
# TODO Logging
# TODO Tests

from bs4 import BeautifulSoup
import requests
import re

class Page:

    def __init__(self, page_url:str, pattern='window\.open\(".*", "_self"\);') -> None:
        self.page_url = page_url
        self.download_url = None
        self.bs4_page = None
        self.re_pattern = pattern


    def request_url_data(self):
        return requests.get(self.page_url, headers={'User-Agent': 'Mozilla/5.0'})


    def load_bs4_page(self):
        # Didn't add None validation to be possible to refresh the url_data
        url_data = self.request_url_data()
        self.bs4_page = BeautifulSoup(url_data.content, "html.parser")


    def extract_download_url(self):
        if self.bs4_page is None:
            self.load_bs4_page()
        page_script = self.bs4_page.find_all("script").__repr__()
        link = re.search('window\.open\(".*", "_self"\);', page_script).group()
        start_index = link.find('"') + 1
        end_index = link[start_index:].find('"') + start_index
        self.download_url = link[start_index:end_index]
        return self.download_url


    # Getters

    def get_bs4_page(self) -> object:
        self.load_bs4_page()
        return self.bs4_page
