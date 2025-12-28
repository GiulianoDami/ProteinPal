class ProteinModel:
    def __init__(self, food_data):
        self.food_data = food_data

    def get_protein_rich_foods(self, preference, min_protein):
        filtered_foods = []
        for food in self.food_data:
            if food['protein'] >= min_protein and preference in food['tags']:
                filtered_foods.append(food['name'])
        return filtered_foods

    def suggest_meals(self, protein_goal, preference):
        meal_options = []
        daily_protein = 0
        for food in self.food_data:
            if preference in food['tags'] and daily_protein + food['protein'] <= protein_goal:
                meal_options.append(food['name'])
                daily_protein += food['protein']
                if daily_protein >= protein_goal:
                    break
        return meal_options

# Example food data structure
food_data_example = [
    {'name': 'Lentil Soup with Spinach and Quinoa Salad', 'protein': 45, 'tags': ['plant']},
    {'name': 'Vegan Chickpea Stew with Brown Rice', 'protein': 35, 'tags': ['plant']},
    {'name': 'Tofu Stir-Fry with Steamed Broccoli and Vegetables Rice Bowl', 'protein': 30, 'tags': ['plant']},
    {'name': 'Grilled Chicken Salad with Mixed Greens', 'protein': 40, 'tags': ['animal']},
    {'name': 'Beef and Broccoli Stir-Fry', 'protein': 50, 'tags': ['animal']},
    {'name': 'Mixed Bean Chili with Sweet Potato', 'protein': 30, 'tags': ['mixed']},
    {'name': 'Turkey and Avocado Wrap', 'protein': 35, 'tags': ['mixed']}
]

# Example usage
if __name__ == "__main__":
    model = ProteinModel(food_data_example)
    print(model.suggest_meals(150, 'plant'))