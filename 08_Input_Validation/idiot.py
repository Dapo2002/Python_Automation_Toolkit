# A recursive-logic simulation utilizing an external validation library to enforce 
# boolean input constraints while creating an infinite loop.

import pyinputplus as pyip

while True:
    response = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?:\n')
    if response == 'no':
        print('Thank you. Have a nice day')
        break
    print(response + ' is not a valid yes/no response')