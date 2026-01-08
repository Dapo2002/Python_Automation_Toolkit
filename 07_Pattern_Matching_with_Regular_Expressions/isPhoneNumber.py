# A manual string-parsing utility that implements a character-validation
# algorithm and a sliding-window search to identify North American
# numbering plan patterns.

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?\n' + str(isPhoneNumber('415-555-4245')) + '\nIs moshi moshi a phone number?\n' + str(isPhoneNumber('moshi')))
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(chunk)