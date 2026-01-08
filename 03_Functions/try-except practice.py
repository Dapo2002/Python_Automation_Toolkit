# A functional division wrapper utilizing a 'try/except' block to catch runtime exceptions 
# and prevent program crashes during invalid arithmetic operations.

def spam(num, dividedby):
    return num / dividedby


try:
    print((spam(float(input('num: ')), float(input('number to divide by: ')))))
except:
    print('Invalid argument')