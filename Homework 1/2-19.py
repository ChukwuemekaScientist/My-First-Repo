# Chukwuemeka Agu
# 1871765

lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(lemon), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar")
print()

desired_servings = float(input("How many servings would you like to make?\n"))
print()

ingredient_adjuster = desired_servings/servings
print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings), "servings")
print('{:.2f}'.format(lemon*ingredient_adjuster), "cup(s) lemon juice")
print('{:.2f}'.format(water*ingredient_adjuster), "cup(s) water")
print('{:.2f}'.format(agave*ingredient_adjuster), "cup(s) agave nectar")
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings), "servings")
print('{:.2f}'.format((lemon*ingredient_adjuster)/16), "gallon(s) lemon juice")
print('{:.2f}'.format((water*ingredient_adjuster)/16), "gallon(s) water")
print('{:.2f}'.format((agave*ingredient_adjuster)/16), "gallon(s) agave nectar")
