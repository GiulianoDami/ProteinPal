# settings.py

# Default protein sources
PROTEIN_SOURCES = {
    'plant': ['lentils', 'chickpeas', 'tofu', 'spinach', 'quinoa'],
    'animal': ['chicken', 'beef', 'salmon', 'eggs', 'milk'],
    'mixed': ['lentils', 'chickpeas', 'tofu', 'spinach', 'quinoa', 'chicken', 'beef', 'salmon', 'eggs', 'milk']
}

# Default meal suggestions
MEAL_SUGGESTIONS = {
    'plant': [
        'Lentil Soup with Spinach and Quinoa Salad',
        'Vegan Chickpea Stew with Brown Rice',
        'Tofu Stir-Fry with Steamed Broccoli and Vegetables Rice Bowl'
    ],
    'animal': [
        'Grilled Chicken Salad with Mixed Greens and Avocado',
        'Beef and Broccoli Stir-Fry',
        'Smoked Salmon with Quinoa Pilaf'
    ],
    'mixed': [
        'Chicken and Lentil Curry',
        'Beef and Spinach Lasagna',
        'Salmon and Tofu Teriyaki Bowl'
    ]
}

# Nutritional values per 100g (approximate)
NUTRITIONAL_VALUES = {
    'lentils': {'protein': 18},
    'chickpeas': {'protein': 19},
    'tofu': {'protein': 8},
    'spinach': {'protein': 2.9},
    'quinoa': {'protein': 14},
    'chicken': {'protein': 31},
    'beef': {'protein': 26},
    'salmon': {'protein': 20},
    'eggs': {'protein': 13},
    'milk': {'protein': 3.4}
}