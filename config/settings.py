# Configuration settings for ProteinPal

# Default protein sources
PROTEIN_SOURCES = {
    'plant': ['lentils', 'chickpeas', 'tofu', 'spinach', 'broccoli'],
    'animal': ['chicken', 'beef', 'salmon', 'eggs', 'milk'],
    'mixed': ['lentils', 'chicken', 'tofu', 'salmon', 'spinach']
}

# Default meal ideas
MEAL_IDEAS = {
    'plant': [
        'Lentil Soup with Spinach and Quinoa Salad',
        'Vegan Chickpea Stew with Brown Rice',
        'Tofu Stir-Fry with Steamed Broccoli and Vegetables Rice Bowl'
    ],
    'animal': [
        'Grilled Chicken Salad with Mixed Greens and Cherry Tomatoes',
        'Beef and Vegetable Stir-Fry with Brown Rice',
        'Smoked Salmon and Avocado Toast'
    ],
    'mixed': [
        'Chicken and Lentil Curry with Quinoa',
        'Beef and Chickpea Stew with Brown Rice',
        'Tofu and Salmon Stir-Fry with Mixed Vegetables'
    ]
}

# Nutritional values per 100g (approximate)
NUTRITIONAL_VALUES = {
    'lentils': {'protein': 18},
    'chickpeas': {'protein': 19},
    'tofu': {'protein': 8},
    'spinach': {'protein': 2.9},
    'broccoli': {'protein': 2.8},
    'chicken': {'protein': 31},
    'beef': {'protein': 26},
    'salmon': {'protein': 20},
    'eggs': {'protein': 13},
    'milk': {'protein': 3.4}
}