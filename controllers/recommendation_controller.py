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
        # Simple logic to select meals. This can be improved with better algorithms.
        meals = []
        current_protein = 0

        for food in foods:
            if current_protein + food['protein'] <= protein_goal:
                meals.append(food['name'])
                current_protein += food['protein']

        return meals



# Sample food data
food_data = [
    {'name': 'Lentil Soup with Spinach and Quinoa Salad', 'type': 'plant', 'protein': 45},
    {'name': 'Vegan Chickpea Stew with Brown Rice', 'type': 'plant', 'protein': 35},
    {'name': 'Tofu Stir-Fry with Steamed Broccoli and Vegetables Rice Bowl', 'type': 'plant', 'protein': 30},
    {'name': 'Grilled Chicken Salad with Mixed Greens', 'type': 'animal', 'protein': 40},
    {'name': 'Beef and Broccoli Stir-Fry', 'type': 'animal', 'protein': 50},
    {'name': 'Turkey and Avocado Wrap', 'type': 'mixed', 'protein': 30},
    {'name': 'Quinoa and Black Bean Tacos with Shredded Chicken', 'type': 'mixed', 'protein': 45}
]

# Example usage
if __name__ == "__main__":
    controller = RecommendationController(food_data)
    protein_goal = 150
    preference = 'plant'
    recommendations = controller.get_recommendations(protein_goal, preference)
    print("Recommended meals:", recommendations)