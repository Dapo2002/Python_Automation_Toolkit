# A cloud-synchronization utility that validates local .xlsx files, uploads them 
# to Google Sheets, and automates server-side rendering into PDF and ODS formats.

from pathlib import Path
import ezsheets

ss = ''
while True:
    prompt = input('Input Filename:\n')
    if Path(prompt).suffix != '.xlsx':
        print('.xlsx extension missing! Add it to your file name')
        continue
    elif Path(prompt).exists():
        print(f'Uploading {prompt}...')
        ss = ezsheets.upload(prompt)
        break
    else:
        print('No such file exist')
        continue

print('Downloading different formats...')
ss.downloadAsPDF()
ss.downloadAsODS()
print('Done!!!')
