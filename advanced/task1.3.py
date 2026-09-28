# Task 1.3: Write a function make_custom_sandwich(ingredients) that takes a list of strings, for example: ["bread", "lettuce", "tomato", "ham", "bread"].

def make_custom_sandwich(ingredients):
    if  any(key_ingredient not in ingredients for key_ingredient in ["ham", "tomato"]):
        return False
    if not ingredients.count("bread") >= 2:
        print("Error: A sandwhich needs top and bottom bread!")
        return
    for ingredient in ingredients:
        print(ingredient)
    
test_ingredients = ["bread", "lettuce", "tomato", "ham", "bread"]
make_custom_sandwich(test_ingredients)
