import bs4
import imapclient
import pyzmail
# import webbrowser

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('gbejiwumi2002@gmail.com', 'uxxxxxxxx')
imapObj.select_folder('INBOX', readonly=True)
uids = imapObj.search(['since', '06-Feb-2026', 'before', '07-Feb-2026'])

rawMessages = imapObj.fetch(uids, ['BODY[]'])
for uid in uids:
    message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])
    messageHTML = message.html_part.get_payload().decode(message.html_part.charset)
    soup = bs4.BeautifulSoup(messageHTML, 'html.parser')
    unsubscibeElem = soup.find_all('a', string=lambda text: text and 'unsubscribe' in text.lower())
    if unsubscibeElem:
        unsubscibeUrl = unsubscibeElem[0].get('href')
        print(f'Opening {unsubscibeUrl}')
        # webbrowser.open(unsubscibeUrl)
    else:
        print('No unsubscribe button found for this mail!')
