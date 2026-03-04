# A GUI automation bot to sequentially search and notify a list of contacts via WhatsApp.

import pyautogui

pyautogui.PAUSE = 1
pyautogui.sleep(5)  # Time to position the whatapp tab
listOfFriends = ['Azeem', 'Faisol', 'Sarz', 'Me', 'Abdulquadri']
try:
    searchBar = pyautogui.locateCenterOnScreen(
        'whatsappSearchBar.png')  # The search bar; NOTE: Based on the resolution of your screen.
    for friend in listOfFriends:
        pyautogui.click(searchBar)
        pyautogui.write(friend)
        pyautogui.press(['enter'])  # Friend's name
        pyautogui.write('A notification message')
        pyautogui.press(['enter'])
except Exception as e:
    print(f'That was close! >>> {e}')
