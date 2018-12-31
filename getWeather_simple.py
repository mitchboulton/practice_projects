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
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

# Reads raw HTML file, and parses it with BeautifulSoup
raw_html = open('Weather_HTML_export.txt').read()
html = BeautifulSoup(raw_html, 'html.parser')

# Collects a list of all items in "p"
textContent = []
for i in range(0, 25):
    paragraphs = html.find_all("p")[i].text
    textContent.append(paragraphs)

# Prints the 5th item in the list, which is the current temp in Celsius
print("Current temperature in Charlotte:",textContent[5])

# Keeps command box open
input("")




