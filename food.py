class Food:
    def __init__(self, name):
        self.name = name
        self.macronutrients = {}
        self.micronutrients = {}

    def add_macronutrient(self, nutrient, amount):
        self.macronutrients[nutrient] = amount

    def add_micronutrient(self, nutrient, amount):
        self.micronutrients[nutrient] = amount

# Example usage:

loop_start = True
foods = []

while loop_start:
    user_input_about_food = input("Enter the name of the product (or type 'done' to finish): ")

    if user_input_about_food.lower() == 'done':
        loop_start = False
        break

    food = Food(user_input_about_food)

    for nutrient_type in ['macronutrients', 'micronutrients']:
        print(f"Enter {nutrient_type} for {user_input_about_food}:")
        nutrients = total_info_about_food_product[nutrient_type]
        for nutrient_dict in nutrients:
            for nutrient, default_value in nutrient_dict.items():
                amount = input(f"{nutrient}: ")
                food.add_macronutrient(nutrient, amount) if nutrient_type == 'macronutrients' else food.add_micronutrient(nutrient, amount)

    foods.append(food)