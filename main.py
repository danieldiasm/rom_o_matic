from downloader.rom_download import ROM

Tekken3_ROM = ROM("Res Evil 4", "https://coolrom.com.au/roms/ps2/41800/Resident_Evil_4.php", "/downloadpath/placeholder")

Tekken3_ROM.extract_download_url()

url = Tekken3_ROM.get_download_url()
game_data = Tekken3_ROM.get_game_data()

print(url)
print(game_data)