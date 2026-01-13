# A terminal-based animation script using variable indentation and 
# boolean direction-toggling to create a rhythmic zig-zag visual effect.

import sys
import time

indent = 0  # How many spaces to indent
indentIncreasing = True  # Check if indent is increasing or not
try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
        if indentIncreasing:
            indent += 1  # Increase the number of spaces
            if indent == 20:
                indentIncreasing = False  # change direction
        else:
            indent -= 1  # Decrease the number of spaces
            if indent == 0:
                indentIncreasing = True  # change direction
except KeyboardInterrupt:
    sys.exit('Welldone')
