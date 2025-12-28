class RecommendationController:
    def __init__(self, food_data):
        self.food_data = food_data

    def get_recommendations(self, protein_goal, preference):
        filtered_foods = self._filter_foods_by_preference(preference)
        recommended_meals = self._select_meals(filtered_foods, protein_goal)
        return recommended_meals

    def _filter_foods_by_preference(self, preference):
        if preference == 'plant':
            return [food for food in self.food_data if food['type'] == 'plant']
        elif preference == 'animal':
            return [food for food in self.food_data if food['type'] == 'animal']
        elif preference == 'mixed':
            return self.food_data
        else:
            raise ValueError("Invalid preference. Please choose 'plant', 'animal', or 'mixed'.")

    def _select_meals(self, foods, protein_goal):
        # Simple algorithm to select meals based on protein content
        selected_meals = []
        current_protein = 0

        for food in sorted(foods, key=lambda x: x['protein'], reverse=True):
            if current_protein < protein_goal:
                selected_meals.append(food['name'])
                current_protein += food['protein']

        return selected_meals



# Sample food data
food_data = [
    {'name': 'Lentil Soup with Spinach and Quinoa Salad', 'type': 'plant', 'protein': 45},
    {'name': 'Vegan Chickpea Stew with Brown Rice', 'type': 'plant', 'protein': 35},
    {'name': 'Tofu Stir-Fry with Steamed Broccoli and Vegetables Rice Bowl', 'type': 'plant', 'protein': 30},
    {'name': 'Grilled Chicken Salad with Mixed Greens', 'type': 'animal', 'protein': 40},
    {'name': 'Beef and Sweet Potato Stew', 'type': 'animal', 'protein': 50},
    {'name': 'Turkey and Avocado Wrap', 'type': 'mixed', 'protein': 38},
    {'name': 'Quinoa and Black Bean Chili', 'type': 'mixed', 'protein': 32}
]

# Example usage
if __name__ == "__main__":
    controller = RecommendationController(food_data)
    protein_goal = 150
    preference = 'plant'
    recommendations = controller.get_recommendations(protein_goal, preference)
    print("Recommended meals:")
    for meal in recommendations:
        print(meal)