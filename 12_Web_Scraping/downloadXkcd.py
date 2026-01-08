#! python3
#  downloadXkcd.py - Downloads ever single XKCD comics

import requests, os, bs4

url = 'https://xkcd.com'  # Starting url
os.makedirs('xkcd', exist_ok=True)  # stores comics in ./xkcd
while len(os.listdir('xkcd')) < 15:
    #  Download the page
    print(f'Downloading the page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #  Find the URL of the comic image
    comicElem = soup.select('#comic img')
    comicUrl = 'https:' + comicElem[0].get('src')
    if not comicElem:
        print('Could not find comic image.')
    else:
        #  Download the image
        print('Downloading image %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

    #  Save the image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # Get the previous button url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
