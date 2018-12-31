import requests
from bs4 import BeautifulSoup

# Pulls Charlotte weather website
res = requests.get('https://forecast.weather.gov/MapClick.php?textField1=35.1975&textField2=-80.8345#.XBwoGFxKhPY')

# Tests for errors
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# Exports to a txt file
playFile = open('Weather_HTML_export.txt', 'wb')
for chunk in res.iter_content(1):
    playFile.write(chunk)
playFile.close()

# Reads raw HTML file, and parses it with BeautifulSoup
raw_html = open('Weather_HTML_export.txt').read()
soup = BeautifulSoup(raw_html, 'html.parser')

# Counts and prints the number of 'P's in the html file
# length = len(soup('p'))
# print("Number of paragraphs: ",length)

# Searches for the relevant location in the HTML document, and pulls out the relevant text
abstract = soup.find('p', attrs={'class' : 'myforecast-current-sm'})
abstract = abstract.text

# Prints the relevant text, which is the current temp in Celsius
print("Current temperature in Charlotte: ",abstract)

# Keeps command box open
input("")
