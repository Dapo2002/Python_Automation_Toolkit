import time
import bs4
import imapclient
import pyzmail
import subprocess
import smtplib
import traceback


def checkAndDownload():
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login('gbejiwumi2002@gmail.com', 'uxxxxxxxxxxxx')

    try:
        imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        imapObj.login('gbejiwumi2002@gmail.com', 'uxxxxxxxxxxxxxxxxx')
        imapObj.select_folder('INBOX', readonly=False)
        uids = imapObj.search(['unseen', 'from', 'gbejiwumi2002@gmail.com', 'subject', 'Bittorrent Download'])

        rawMessages = imapObj.fetch(uids, ['BODY[]'])

        secretKey = '123456'
        for uid in uids:
            message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])
            messageText = message.text_part.get_payload().decode(message.text_part.charset)
            if secretKey not in messageText:
                smtpObj.sendmail('gbejiwumi2002@gmail.com', 'gbejiwumi2002@gmail.com',
                                 'Subject: FAILED!\nUnauthorized command attempt.')
                continue
            messageHTML = message.html_part.get_payload().decode(message.html_part.charset)
            soup = bs4.BeautifulSoup(messageHTML, 'html.parser')
            torrentLink = soup.find_all('a', href=True)
            for link in torrentLink:
                url = link['href']
                if url.startswith('magnet') or url.endswith('.torrent'):
                    subprocess.Popen([r'C:\Users\Abdulbadie\AppData\Roaming\BitTorrent Web\btweb.exe', url])
                    smtpObj.sendmail('gbejiwumi2002@gmail.com', 'gbejiwumi2002@gmail.com',
                                     'Subject: Command executed!\nBittorrent download completed.')
                    print(f'Triggered {url}')
        imapObj.delete_messages(uids)
        imapObj.expunge()
        imapObj.logout()
    except Exception:
        try:
            smtpObj.sendmail('gbejiwumi2002@gmail.com', 'gbejiwumi2002@gmail.com',
                             f'Subject: ERROR!\n{traceback.format_exc()}')
        except Exception as email_err:
            print(f'Could not send error mail: {email_err}')
    smtpObj.quit()


while True:
    checkAndDownload()
    time.sleep(15*60)
