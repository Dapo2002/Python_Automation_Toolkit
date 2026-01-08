# A demonstration of exception propagation through a nested call stack, 
# illustrating how 'raise' halts execution and bubbles up through the parent 
# functions.

def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


spam()
