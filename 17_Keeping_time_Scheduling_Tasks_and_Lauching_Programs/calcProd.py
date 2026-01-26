# Calculates the factorial of 99,999 and measures the execution time of the computation.
# Disables Python's integer-to-string conversion limit to allow processing of the resulting massive digit count.

import sys
import time

sys.set_int_max_str_digits(0)


def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product *= i
    return product


startTime = time.time()
prod = calcProd()
print(f'The result is {len(str(prod))} digits long.')
endTime = time.time()
print(f'Took {endTime - startTime} seconds to calculate.')
