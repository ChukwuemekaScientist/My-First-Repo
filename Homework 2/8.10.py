# Chukwuemeka Agu
# 1871765

word = input().strip()

reverse_word = word[::-1].strip()

if word.strip() == reverse_word.strip():
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')
