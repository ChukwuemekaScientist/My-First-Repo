# Chukwuemeka Agu
# 1871765

first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
fifth = int(input())
sixth = int(input())


count = 0
for x in range (-10, 10):
    for y in range(-10, 10):
        if ((first*x) + (second*y) == third) and ((fourth*x) + (fifth*y) == sixth):
            print (x, y)
            count =+ 1
        else:
            continue

if count == 0:
    print("No solution")
