import requests
from bs4 import BeautifulSoup as bs
import json

# TODO: Make OOP
# TODO: Function for downloading images
# TODO: Function for downloading videos
# TODO: Script to create Evernote notes from JSON, image, and video files

def scrape_recipe(url):
    
    # get page content
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    
    # find json data
    raw = soup.find('script', {'type': 'application/ld+json'})

    return str(raw.text)


if __name__ == '__main__':
    # URL = 'https://www.pannacooking.com/recipes/smoky-veggie-chili/'
    # scrape_recipe(URL)

    with open('./data/all-recipe-urls.dat', 'r', encoding='utf-8-sig') as f:
        url_list = [x.strip() for x in f.readlines()]
    
    i = 0 # counter
    for url in url_list:
        print(i, url.split('/')[-2])

        with open('./output/' + url.split('/')[-2] + '.json', 'w') as o:
            o.write(scrape_recipe(url=url))

        i += 1
