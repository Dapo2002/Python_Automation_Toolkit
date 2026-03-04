# This script simulates activity by clicking a
# fixed coordinate and nudging the cursor every 10 seconds.

import pyautogui

print('Press Ctrl-C to stop the script')
try:
    pyautogui.PAUSE = 0.5
    while True:
        pyautogui.click(459, 482)
        pyautogui.move(5, 0)
        pyautogui.sleep(10)
except KeyboardInterrupt:
    print('\nScript stopped!')
