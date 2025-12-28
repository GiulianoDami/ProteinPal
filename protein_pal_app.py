def get_protein_goal():
    return int(input("Welcome to ProteinPal!\nPlease enter your daily protein target (in grams): "))

def get_dietary_preference():
    preference = input("Do you prefer plant-based, animal-based, or mixed meals? (Enter plant/animal/mixed): ").strip().lower()
    while preference not in ['plant', 'animal', 'mixed']:
        print("Invalid input. Please try again.")
        preference = input("Do you prefer plant-based, animal-based, or mixed meals? (Enter plant/animal/mixed): ").strip().lower()
    return preference

def suggest_meals(protein_goal, dietary_preference):
    # Basic dataset of foods with known nutritional values
    foods = {
        'plant': [
            {'name': 'Lentil Soup with Spinach and Quinoa Salad', 'protein': 25},
            {'name': 'Vegan Chickpea Stew with Brown Rice', 'protein': 30},
            {'name': 'Tofu Stir-Fry with Steamed Broccoli and Vegetables Rice Bowl', 'protein': 28}
        ],
        'animal': [
            {'name': 'Grilled Chicken Salad with Mixed Greens', 'protein': 35},
            {'name': 'Beef and Broccoli Stir-Fry', 'protein': 40},
            {'name': 'Shrimp and Vegetable Stir-Fry', 'protein': 38}
        ],
        'mixed': [
            {'name': 'Chicken and Quinoa Bowl with Roasted Vegetables', 'protein': 32},
            {'name': 'Turkey and Avocado Wrap', 'protein': 27},
            {'name': 'Fish and Bean Chili', 'protein': 36}
        ]
    }

    meal_options = foods[dietary_preference]
    suggested_meals = []

    for meal in meal_options:
        if meal['protein'] >= protein_goal / 3:  # Assuming 3 meals a day
            suggested_meals.append(meal['name'])

    return suggested_meals

def main():
    protein_goal = get_protein_goal()
    dietary_preference = get_dietary_preference()
    meal_options = suggest_meals(protein_goal, dietary_preference)

    print("\nHere are your meal options:")
    for i, meal in enumerate(meal_options, 1):
        print(f"{i}. {meal}")

if __name__ == "__main__":
    main()