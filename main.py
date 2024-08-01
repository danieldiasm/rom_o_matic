from downloader.rom_download import ROM

Tekken3_ROM = ROM("Tekken 3", "https://coolrom.com.au/roms/psx/39719/Tekken_3.php", "/downloadpath/placeholder")

Tekken3_ROM.extract_download_url()

url = Tekken3_ROM.get_download_url()

print(url)