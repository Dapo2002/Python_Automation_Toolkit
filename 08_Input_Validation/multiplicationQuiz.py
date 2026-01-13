# A timed mental-math simulator utilizing 'pyinputplus' for regex-driven answer 
# validation, concurrency-based timeouts, and retry-limit enforcement.

import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        #  Right Answers are handles by allowRegexes
        #  Wrong Answers are handles by blockRegexes
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Invalid Answer!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:  # This code runs if no exceptions were raised in the try block
        print('Correct Answer!')
        correctAnswers += 1
    time.sleep(1)  # Lets the user see the result
print(f'Score: {correctAnswers} / {numberOfQuestions}')
