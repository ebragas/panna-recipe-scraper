from panna.helpers import Panna
import requests
import json


if __name__ == "__main__":
    panna = Panna(start_url="https://api.pannacooking.com/recipes")
    panna.get_recipes()
    
    with open('recipes.json', 'a') as fp:
        for recipe in panna.recipes:
            json.dump(recipe, fp)
            fp.write(',\n')
    
    print('Done!')

# querystring = {"page":"1","page_size":"24","sort_by":"publishDate","sort_order":"DESC","hide_for_lesson_only":"true"}
# payload = ""