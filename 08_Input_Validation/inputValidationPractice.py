# A robust input-sanitization loop utilizing 'try/except' blocks for type-
# checking and conditional branching for domain-specific boundary validation.

while True:
    age = input('Enter your age:\n')
    try:
        age = int(age)
    except ValueError as e:
        print(f'{e}')
        continue
    if age < 1:
        print('Age cannot be less than 1')
        continue
    break

print(f'Your age is {age}')
