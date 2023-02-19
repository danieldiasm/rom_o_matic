# Downloadlink exrtactor

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

# Have the target URL
url = "https://coolrom.com.au/roms/psx/39719/Tekken_3.php"

# Retrieve the URL data and decode to UTF-8
# It is important to add a header to act as a browser, otherwise a 403 will come as response
page = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
result = urlopen(page).read().decode('utf-8')

# Create a new BS object
soup = BeautifulSoup(result, "html.parser")

# Retrieve only the "script" tag sections of the page text calling the repr method
page_script = soup.find_all("script").__repr__()

# Then clean up taking only the part that shows window.open( bla bla bla until "_self");
# Note that we had to escape special characters used by the regex
download_link = re.search('window\.open\(".*", "_self"\);',page_script).group()

# Then we remove what doesn't matter to us, we want just the generated link
start_index = download_link.find('"') + 1
end_index = download_link[start_index:].find('"') + start_index

# Finally extract the link
result = download_link[start_index:end_index]

# This is the result
print(download_link[start_index:end_index])

# It can be converted into a class with methods for the extraction
