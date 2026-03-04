# This script safely captures all text from an open Notepad window by finding its position,
# activating it, and using keyboard hotkeys to copy the content to the clipboard.

import pyautogui
import pyperclip

pyautogui.PAUSE = 0.5
fw = pyautogui.getWindowsWithTitle('notepad')
if not fw or fw[0].isMinimized:
    exit()
windowPosition = fw[0].topleft
fw[0].activate()
pyautogui.click(windowPosition[0] + 200, windowPosition[1] + 200)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
fw[0].minimize()
copiedText = pyperclip.paste()
print(copiedText)
