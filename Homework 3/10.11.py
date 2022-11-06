# Chukwuemeka Agu
# 1871765

class FoodItem:
    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


name_i = input()
fat_i = float(input())
carbs_i = float(input())
protein_i = float(input())
servings_i = float(input())

item1 = FoodItem()
item1.print_info()
print(f"Number of calories for {servings_i:.2f} serving(s): {item1.get_calories(servings_i):.2f}")
print()

item2 = FoodItem(name_i, fat_i, carbs_i, protein_i)
item2.print_info()
print(f"Number of calories for {servings_i:.2f} serving(s): {item2.get_calories(servings_i):.2f}")