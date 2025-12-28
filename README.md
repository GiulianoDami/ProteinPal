PROJECT_NAME: ProteinPal

## Description
ProteinPal is a simple Python project designed to help users manage their protein intake in a tastier and healthier way. Given that many consumers seek to increase their protein consumption but struggle with the unpalatable nature of many protein-rich supplements, ProteinPal provides personalized meal suggestions that are rich in protein and customizable based on dietary preferences (plant-based, meat-based, etc.). It uses a basic dataset of foods with known nutritional values and can be easily extended with more detailed data for better accuracy.

## Installation
To install and use ProteinPal on your local machine, follow these steps:

1. **Clone the repository:**
   bash
   git clone https://github.com/yourusername/ProteinPal.git
   cd ProteinPal
   

2. **Install dependencies:**
   bash
   pip install -r requirements.txt
   

3. **Run the application:**
   bash
   python protein_pal_app.py
   

*Note: Ensure you have Python installed on your system before cloning the repository. You can download Python from [python.org](https://www.python.org/downloads/).*

## Usage
Once installed, the ProteinPal application can be used to receive meal recommendations based on your desired protein intake and dietary preferences. Here's how to use it:

- Run the `protein_pal_app.py` file.
- Follow the prompts to enter your daily protein goal and specify whether you prefer plant-based, animal-based, or mixed protein sources.
- Receive a list of meal ideas that meet your protein requirements.

### Example Interaction
plaintext
Welcome to ProteinPal!
Please enter your daily protein target (in grams): 150
Do you prefer plant-based, animal-based, or mixed meals? (Enter plant/animal/mixed): plant
Here are your meal options:
1. Lentil Soup with Spinach and Quinoa Salad
2. Vegan Chickpea Stew with Brown Rice
3. Tofu Stir-Fry with Steamed Broccoli and Vegetables Rice Bowl


### Extending the Application
To extend ProteinPal with more detailed food data or additional features:
- Modify the `food_data.json` file to include more food items and their respective protein content.
- Add new functions or modify existing ones in `protein_pal_logic.py` to handle different dietary needs or to provide more diverse meal recommendations.
- Update the `protein_pal_app.py` script to reflect any changes in logic or input handling.

This project aims to make healthy protein consumption more appealing and accessible, encouraging users to meet their nutritional goals without relying solely on supplements.