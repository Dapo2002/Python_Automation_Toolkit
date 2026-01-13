# A manual implementation of a timed-input state machine that utilizes delta-time 
# calculations and nested 'for-if-else' loops to manage retry logic and temporal 
# constraints.

import random
import time

numOfQuestions = 10
correctAnswer = 0
for i in range(1, numOfQuestions+1):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    isCorrect = False
    tries = 3
    for j in range(tries):
        startTime = time.time()
        raw = input(f'#{i}: {num1} x {num2} = ')
        timeout = time.time()

        if timeout - startTime > 8:
            print('Timeout!')
            break

        try:
            prompt = int(raw)
        except ValueError as e:
            print(f'Error: {e}, Try again!')
            continue

        if prompt == num1 * num2:
            print('Correct!')
            time.sleep(1)
            isCorrect = True
            correctAnswer += 1
            break
        else:
            if j < tries - 1:
                print('Try Again!')
            elif i >= numOfQuestions - 1:
                print()
            else:
                print('Out of tries! Next question...')
        continue
print(f'{correctAnswer} / {numOfQuestions}')
