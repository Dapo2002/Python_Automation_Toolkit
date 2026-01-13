#  searchpypi.py - Opens several search results.

import bs4
from pathlib import Path
import webbrowser

print('Searching...')  # display text while downloading the search result page
res = open(Path.cwd()/'Search results · PyPI.html', encoding='utf-8', errors='ignore')

#  Retrieve top search result links.
soup = bs4.BeautifulSoup(res.read(), 'html.parser')
res.close()
#  Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
