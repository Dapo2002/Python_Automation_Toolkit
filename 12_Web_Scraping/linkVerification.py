# A focused web crawler that identifies and validates contextual hyperlinks 
# within Wikipedia paragraphs, performing automated status-checks on the 
# discovered knowledge network.

import time
import bs4
import requests

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/118.0 Safari/537.36"
    )
}
res = requests.get('https://en.wikipedia.org/wiki/Clinical_psychology', headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('p a[href][title]')
for link in links:
    url = 'https://en.wikipedia.org' + link.get('href')
    try:
        downloadLink = requests.get(url, headers=headers)
        time.sleep(1)
        downloadLink.raise_for_status()
        print(f'✅ {url} downloaded successfully!')
    except Exception as e:
        print(f'{e} >>> Broken Link')
