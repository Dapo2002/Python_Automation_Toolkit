# An implementation of the Collatz Conjecture featuring input validation and an O(???) recursive-style iterative sequence # that terminates at 1.

def collatz(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
    print(1)
    return number


while True:
    try:
        userInput = int(input('Enter a number: '))
        if userInput <= 0:
            print('Error: Can\'t input anything below 1')
        else:
            collatz(userInput)
            break
    except ValueError as e:
        print(f'Error: {e}')
