# A custom input-validation engine that utilizes 'inputCustom' to map a sequence 
# of characters to a summation algorithm, enforcing specific arithmetic 
# properties via raised Exceptions.

import pyinputplus as pyip


def addsUpTo10(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception(f'Sum of number must be 10 not {sum(numbersList)}.')
    return int(numbers)


response = pyip.inputCustom(addsUpTo10)