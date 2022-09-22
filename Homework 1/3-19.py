# Chukwuemeka Agu
# 1871765

wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
wall_area = wall_width*wall_height
print("Wall area:", wall_area, "square feet")

gallons_paint = float(wall_area/350)
print("Paint needed:", '{:.2f}'.format(gallons_paint), "gallons")

cans_needed = round(gallons_paint)
print("Cans needed:", cans_needed, "can(s)")

color = input("\nChoose a color to paint the wall:\n")
colors_dict = {'red': 35, 'blue': 25, 'green': 23}

print("Cost of purchasing", color, "paint:", f'${colors_dict[color]*cans_needed}')