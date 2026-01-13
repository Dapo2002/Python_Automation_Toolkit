# A password-complexity auditor that utilizes a series of independent regex 
# pattern-matches to enforce minimum length and character-set diversity 
# requirements.

import re


def strongPassword(somePassword):
    passwordLength = re.compile(r'.{8,}')
    atLeastOneUpperCase = re.compile(r'[A-Z]+')
    atLeastOneLowerCase = re.compile(r'[a-z]+')
    atLeastOneDigit = re.compile(r'\d+')

    if not passwordLength.findall(somePassword):
        return 'Weak password: Password length less than 8 characters'
    elif not atLeastOneUpperCase.findall(somePassword):
        return 'Weak password: Password must contain at least an uppercase letter'
    elif not atLeastOneLowerCase.findall(somePassword):
        return 'Weak password: Password must contain at least an lowercase letter'
    elif not atLeastOneDigit.findall(somePassword):
        return 'Weak password: Password must contain at least a digit'
    else:
        return True


while True:
    password = input('Enter your password:\n')
    result = strongPassword(password)
    if result is True:
        print('Password strength passed!')
        break
    print(result)
