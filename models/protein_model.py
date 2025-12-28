class ProteinModel:
    def __init__(self, food_data):
        self.food_data = food_data

    def get_meal_options(self, protein_goal, preference):
        meal_options = []
        for food in self.food_data:
            if preference == 'mixed' or food['type'] == preference:
                if food['protein'] >= protein_goal / 3:  # Assuming a meal consists of 3 food items
                    meal_options.append(food['name'])
        return meal_options

    def suggest_meals(self, protein_goal, preference):
        meal_options = self.get_meal_options(protein_goal, preference)
        suggested_meals = []
        current_protein = 0

        while current_protein < protein_goal and len(meal_options) > 0:
            meal = meal_options.pop(0)
            for food in self.food_data:
                if food['name'] == meal:
                    suggested_meals.append(meal)
                    current_protein += food['protein']
                    break

        return suggested_meals