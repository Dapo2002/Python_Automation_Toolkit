#! python3
# scheduledWebComicDownloader.py - An automated web scraper that monitors xkcd.com for updates.
# Uses persistence logic via a local log file to ensure images are only downloaded
# when a new comic is published, minimizing bandwidth and disk usage.

import os
import requests
import bs4
import time

desktop = r'C:\Users\Abdulbadie\OneDrive\Desktop'
logFile = os.path.join(desktop, 'last_xkcd.txt')
os.makedirs(desktop, exist_ok=True)

while True:
    print(f'Downloading page https://xkcd.com/')
    res = requests.get(f'https://xkcd.com/')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image')
    else:
        comicUrl = comicElem[0].get('src')

        needsDownload = True

        if os.path.exists(logFile):
            with open(logFile) as log:
                if log.read() == comicUrl:
                    print('No new comic found')
                    needsDownload = False  # We already have it!

        if needsDownload:
            print(f'New comic found! Downloading image {comicUrl}')
            res = requests.get(f'https:{comicUrl}')
            res.raise_for_status()
            with open(f'{os.path.join(desktop, os.path.basename(comicUrl))}', 'wb') as imageFile:
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)

            # Update the log
            with open(logFile, 'w') as log:
                log.write(comicUrl)

            print('Done.')
    time.sleep(24 * 60 * 60)
