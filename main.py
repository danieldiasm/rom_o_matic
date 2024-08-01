from downloader.rom_download import ROM

Tekken3_ROM = ROM("Tekken 3", "https://some-rom-page.com", "/downloadpath/placeholder")

Tekken3_ROM.extract_download_url()

url = Tekken3_ROM.get_download_url()

print(url)