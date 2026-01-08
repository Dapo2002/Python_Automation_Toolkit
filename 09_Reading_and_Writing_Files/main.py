from pathlib import Path

p = Path('C:/Users/User/Desktop')
for textFilePathObj in p.glob('*'):
    print(textFilePathObj)
print(p.is_file())
print('\n', Path.cwd())
