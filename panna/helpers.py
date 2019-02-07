import requests
import json
import time

class Panna():
    def __init__(self, start_url):
        self.url = start_url
        self.recipes = []

    def get_recipes(self):

        response = requests.get(self.url).json()
        
        self.recipes.extend(response['_embedded']['recipes'])
        self_page = response['_links']['self']['href']
        last_page = response['_links']['last']['href']
        
        if self_page != last_page:
            time.sleep(1)
            self.url = response['_links']['next']['href']
            self.get_recipes()
        