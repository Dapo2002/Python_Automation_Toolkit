# Creates custom 288x360 name cards with a red background, black border,
# flower graphic, and gold-centered text for each guest listed in 'guests.txt'.

from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs(r'C:\Users\User\OneDrive\User\PycharmProjects\My_Python_for_Automation_Journey'
            r'\19_Manipulating_Images\seatCardFolder', exist_ok=True)
folder = r'C:\Users\User\OneDrive\User\PycharmProjects\My_Python_for_Automation_Journey' \
         r'\19_Manipulating_Images\seatCardFolder'
guestFileObj = open('guests.txt')
guests = guestFileObj.readlines()
flowerObj = Image.open('flower.png')
flowerObj = flowerObj.convert('RGBA')
flowerResized = flowerObj.resize((278, 350))
font = ImageFont.truetype(r'C:\Windows\Fonts\Corbel.ttf', 30)

for guest in guests:
    guest = guest.strip()
    card = Image.new('RGBA', (288, 360), 'red')
    draw = ImageDraw.Draw(card)
    draw.rectangle((0, 0, 287, 359), outline='black', width=3)
    card.paste(flowerResized, (5, 5), flowerResized)
    draw.text((card.size[0]/2, card.size[1]/2), guest, 'gold', font=font, anchor='mm')
    card.save(os.path.join(folder, f'seatCard_{guest}.png'))
