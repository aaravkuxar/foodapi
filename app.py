from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Sample recipes data
recipes_data = {
    "success": "true",
    "message": "Recipes fetched successfully.",
    "payload": [
        {
            "_id": "6405721fa13d0d2d35890e0d",
            "Recipe_id": "2774",
            "Calories": "237.0",
            "cook_time": "65",
            "prep_time": "40",
            "servings": "6",
            "Recipe_title": "Moroccan Potato Casserole",
            "total_time": "105",
            "url": "http://allrecipes.com/recipe/13905/moroccan-potato-casserole/",
            "Region": "Rest Africa",
            "Sub_region": "Nigerian",
            "Continent": "African",
            "Source": "AllRecipes",
            "img_url": "https://images.media-allrecipes.com/userphotos/250x250/954160.jpg",
            "Carbohydrate, by difference (g)": "146.3439",
            "Energy (kcal)": "1030.6311",
            "Protein (g)": "22.2814",
            "Total lipid (fat) (g)": "44.2194",
            "Utensils": "oven||processor||bowl||bowl||dish",
            "Processes": "preheat||combine||process||add||blend||add||blend||season||season||transfer||scatter||drizzle||cover||bake||remove||serve",
            "vegan": "1.0",
            "pescetarian": "1.0",
            "ovo_vegetarian": "0.0",
            "lacto_vegetarian": "0.0",
            "ovo_lacto_vegetarian": "0.0"
        },
        {
            "_id": "6405721fa13d0d2d35890e0e",
            "Recipe_id": "2780",
            "Calories": "320.0",
            "cook_time": "50",
            "prep_time": "20",
            "servings": "4",
            "Recipe_title": "Spicy Lentil Stew",
            "total_time": "70",
            "url": "http://allrecipes.com/recipe/15305/spicy-lentil-stew/",
            "Region": "Middle East",
            "Sub_region": "Lebanese",
            "Continent": "Asian",
            "Source": "AllRecipes",
            "img_url": "https://images.media-allrecipes.com/userphotos/250x250/654322.jpg",
            "Carbohydrate, by difference (g)": "120.8439",
            "Energy (kcal)": "880.5311",
            "Protein (g)": "30.7814",
            "Total lipid (fat) (g)": "14.1194",
            "Utensils": "pot||spoon||bowl||ladle",
            "Processes": "heat||add||simmer||stir||serve",
            "vegan": "1.0",
            "pescetarian": "1.0",
            "ovo_vegetarian": "0.0",
            "lacto_vegetarian": "1.0",
            "ovo_lacto_vegetarian": "1.0"
        },
        {
            "_id": "6405721fa13d0d2d35890e0f",
            "Recipe_id": "2791",
            "Calories": "550.0",
            "cook_time": "90",
            "prep_time": "30",
            "servings": "8",
            "Recipe_title": "Italian Lasagna",
            "total_time": "120",
            "url": "http://allrecipes.com/recipe/23234/italian-lasagna/",
            "Region": "Europe",
            "Sub_region": "Italian",
            "Continent": "European",
            "Source": "AllRecipes",
            "img_url": "https://images.media-allrecipes.com/userphotos/250x250/554211.jpg",
            "Carbohydrate, by difference (g)": "160.8439",
            "Energy (kcal)": "1450.5311",
            "Protein (g)": "45.7814",
            "Total lipid (fat) (g)": "60.2194",
            "Utensils": "oven||pan||spatula||baking dish",
            "Processes": "preheat||layer||bake||serve",
            "vegan": "0.0",
            "pescetarian": "0.0",
            "ovo_vegetarian": "0.0",
            "lacto_vegetarian": "1.0",
            "ovo_lacto_vegetarian": "1.0"
        }
    ]
}

@app.route('/recipes', methods=['GET'])
def get_recipes():
    # Return JSON response with multiple recipes
    return jsonify(recipes_data)

@app.route('/recipeOftheDay', methods=['GET'])
def recipe_of_the_day():
    # Select a random recipe from the payload
    recipe = random.choice(recipes_data["payload"])
    response = {
        "success": "true",
        "message": "Recipe of the Day fetched successfully.",
        "payload": recipe
    }
    return jsonify(response)

@app.route('/recipes/<id>', methods=['GET'])
def get_recipe_by_id(id):
    # Find the recipe with the matching Recipe_id
    recipe = next((recipe for recipe in recipes_data["payload"] if recipe["Recipe_id"] == id), None)
    
    # If recipe is found, return it; otherwise, return a 404 error
    if recipe:
        response = {
            "success": "true",
            "message": "Recipe fetched successfully.",
            "payload": recipe
        }
    else:
        response = {
            "success": "false",
            "message": "Recipe not found."
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
