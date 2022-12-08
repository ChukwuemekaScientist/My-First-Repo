# Chukwuemeka Agu
# 1871765

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        if type(age) == 'str':
            raise ValueError

    except ValueError:
        age = 0

    print(f'{name} {age}')
    # Get next line
    parts = input().split()
    name = parts[0]