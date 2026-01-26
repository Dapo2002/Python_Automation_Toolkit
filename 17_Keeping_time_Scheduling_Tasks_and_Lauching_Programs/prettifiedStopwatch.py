#! python3
# prettifiedStopwatch.py - A precision lap timer with dynamic f-string padding and clipboard export.
# Tracks elapsed time, calculates individual lap durations, and copies the formatted log to the clipboard on exit.

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to click the stopwatch.'
      ' Press Ctrl-C to quit.')
input()                         # Press Enter to begin
print('Started.')
startTime = time.time()         # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
output = []
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        result = f'Lap #{lapNum:<2}: {totalTime:>6} ({lapTime:>6})'
        print(result, end='')
        output.append(result)
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\n\nDone.')
    outputString = '\n'.join(output)
    pyperclip.copy(outputString)
