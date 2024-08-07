# Data Extractor

class GameData:

    @staticmethod
    def extract(bs4_page):
        game_data = {}
        
        tables = bs4_page.td.table.find_all('b')

        for b in tables:
            if b.text == 'Game:':
                game_data['title'] = b.next_element.next_element.next_element.contents[0]
            if b.text == 'File Name:':
                game_data['file_name'] = str(b.next_element.next_element.string).strip()
            if b.text == 'File Size:':
                game_data['file_size'] = str(b.next_element.next_element.string).strip()
            if b.text == 'Genre:':
                game_data['genre'] = b.next_element.next_element.next_element.next_element.contents[0]
            if b.text == 'System:':
                game_data['system'] = b.next_element.next_element.next_element.next_element.contents[0]

        return game_data
