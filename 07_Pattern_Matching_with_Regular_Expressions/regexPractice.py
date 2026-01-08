# A regex-based syntax validator that uses anchors (^ and $) to enforce full-
# string matching and 're.I' for case-insensitive lexical verification.

import re

number = re.compile(r'^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$', re.I)

text = ['BOB EATS CATS.',
        'Alice throws Apples.',
        'RoboCop eats apples.',
        'ALICE THROWS FOOTBALLS.',
        'Carol eats 7 cats.',
        'Alice eats apples.',
        'Bob pets cats.',
        'Carol throws baseballs.'
        ]
for sentence in text:
    print(number.findall(sentence))
