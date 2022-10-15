# Chukwuemeka Agu
# 1871765


def exact_change(user_total):
    total_cents = user_total
    nums_dollars = 0
    nums_quarters = 0
    nums_dimes = 0
    nums_nickels = 0
    nums_pennies = 0

    while total_cents>0:
        if total_cents >= 100:
            while total_cents >= 100:
                total_cents -= 100
                nums_dollars += 1
        if total_cents >= 25:
            while total_cents >= 25:
                total_cents -= 25
                nums_quarters += 1
        if total_cents >= 10:
            while total_cents >= 10:
                total_cents -= 10
                nums_dimes += 1
        if total_cents >= 5:
            while total_cents >= 5:
                total_cents -= 5
                nums_nickels += 1
        if total_cents >= 1:
            while total_cents >= 1:
                total_cents -= 1
                nums_pennies += 1

    return nums_dollars, nums_quarters, nums_dimes, nums_nickels, nums_pennies


input_val = int(input())

num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

if input_val <= 0:
    print ("no change")
if num_dollars > 1:
    print (f'{num_dollars} dollars')
elif num_dollars == 1:
    print("1 dollar")
if num_quarters > 1:
    print (f'{num_quarters} quarters')
elif num_quarters == 1:
    print("1 quarter")
if num_dimes > 1:
    print (f'{num_dimes} dimes')
elif num_dimes == 1:
    print("1 dime")
if num_nickels > 1:
    print (f'{num_nickels} nickels')
elif num_nickels == 1:
    print("1 nickel")
if num_pennies > 1:
    print (f'{num_pennies} pennies')
elif num_pennies == 1:
    print("1 penny")