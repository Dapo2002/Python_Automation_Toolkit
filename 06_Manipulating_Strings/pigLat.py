# English to Pig Latin

message = input('Enter the English message to convert into Pig Latin:\n')
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = []  # A list of words in Pig Latin
for word in message.split():
    # Separate the non-letters at the start of each word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    # Separate the non-letters at the end of this word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or titlecase
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # Make the word lowercase for translation
    # Separate the consonant at the start of this word
    prefixConsonant = ''
    while len(word) > 0 and word[0] not in vowels:
        prefixConsonant += word[0]
        word = word[1:]

    # Add the pig latin ending to the word
    if prefixConsonant != '':
        word += prefixConsonant + 'ay'
    else:
        word += 'yay'

    # Set the word back to upper or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words together into a single string
print(' '.join(pigLatin))
