def get_protein_target():
    return int(input("Welcome to ProteinPal!\nPlease enter your daily protein target (in grams): "))

def get_dietary_preference():
    preference = input("Do you prefer plant-based, animal-based, or mixed meals? (Enter plant/animal/mixed): ").strip().lower()
    while preference not in ['plant', 'animal', 'mixed']:
        print("Invalid input. Please try again.")
        preference = input("Do you prefer plant-based, animal-based, or mixed meals? (Enter plant/animal/mixed): ").strip().lower()
    return preference

def suggest_meals(protein_target, dietary_preference):
    # Basic dataset of foods with known nutritional values
    foods = {
        'lentil soup with spinach and quinoa salad': {'protein': 20, 'type': 'plant'},
        'vegan chickpea stew with brown rice': {'protein': 18, 'type': 'plant'},
        'tofu stir-fry with steamed broccoli and vegetables rice bowl': {'protein': 25, 'type': 'plant'},
        'grilled chicken breast with roasted vegetables': {'protein': 30, 'type': 'animal'},
        'baked salmon with quinoa and asparagus': {'protein': 24, 'type': 'animal'},
        'chicken and vegetable stir-fry': {'protein': 22, 'type': 'mixed'},
        'beef and broccoli bowl': {'protein': 26, 'type': 'mixed'}
    }

    meal_options = []
    for food, details in foods.items():
        if details['type'] == dietary_preference or dietary_preference == 'mixed':
            meal_options.append(food)

    # Filter meals based on protein content
    recommended_meals = [meal for meal in meal_options if foods[meal]['protein'] >= protein_target / 3]

    if not recommended_meals:
        return "No meal options match your criteria. Consider adjusting your protein target or dietary preference."

    return "\nHere are your meal options:\n" + "\n".join(f"{i+1}. {meal}" for i, meal in enumerate(recommended_meals))

def main():
    protein_target = get_protein_target()
    dietary_preference = get_dietary_preference()
    print(suggest_meals(protein_target, dietary_preference))

if __name__ == "__main__":
    main()