from cool_rom.rom_data import ROM

ResEvil4_ROM = ROM("Res Evil 4", "https://coolrom.com.au/roms/psx/68727/Resident_Evil_(Europe).php", "/downloadpath/placeholder")

ResEvil4_ROM.extract_game_download_url()

url = ResEvil4_ROM.get_download_url()
game_data = ResEvil4_ROM.get_game_data()

print(url)
print(game_data)