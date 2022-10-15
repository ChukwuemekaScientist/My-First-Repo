# Chukwuemeka Agu
# 1871765

boy = input()
password = ''
for character in boy:
    if character == 'i':
        password += '!'
    elif character == 'a':
        password += '@'
    elif character == 'm':
        password += 'M'
    elif character == 'B':
        password += '8'
    elif character == 'o':
        password += '.'
    else:
        password += character

print(password+ 'q*s')