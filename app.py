from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

recipes_data = {
  "success": "true",
  "message": "Recipes fetched successfully.",
  "payload": {
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
  }
}

@app.route('/recipes', methods=['GET'])
def get_recipes():
    # Return JSON response with multiple recipes
    return jsonify(recipes_data)

@app.route('/recipeOftheDay', methods=['GET'])
def recipe_of_the_day():
    return jsonify(recipes_data)

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
