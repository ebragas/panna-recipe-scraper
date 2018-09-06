import json
import os
import requests as r

# TODO: Add try catch to methods to ensure state consistency

output_dir = os.getcwd() + '/output/'

class Recipe():
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = output_dir + 'json/' + file_name
        
        # Read recipe file contents
        with open(self.file_path, 'r') as f:
            recipe_json = json.load(f)

        # Parse attributes        
        self.name = recipe_json['name']
        self.description = recipe_json['description']
        self.img_url = recipe_json['image']
        self.cook_time = recipe_json['cookTime']
        self.prep_time = recipe_json['prepTime']
        self.ingredients = recipe_json['recipeIngredient']
        self.instructions = recipe_json['recipeInstructions']
        self.recipe_yield = recipe_json['recipeYield']
        self.totalTime = recipe_json['totalTime']
        self.panna_url = recipe_json['url']
        self.video_url = recipe_json['video']['contentURL']
        self.video_transcript = recipe_json['video']['transcript']
        self.video_upload_date = recipe_json['video']['uploadDate']

        self.img_file_path = None
        self.video_file_path = None
        
        print('Instantiated recipe: {}'.format(self.name))

    def download_img(self):
        '''Download recipe image file to image output folder.'''
        # File metadata
        file_ext = self.img_url[self.img_url.find('.', len(self.img_url) - 5):]
        self.img_file_path = output_dir + 'images/' + self.file_name.replace('.json', file_ext)

        # Check if file exists
        if not os.path.isfile(self.img_file_path):
            
            # Download file
            img = r.get(self.img_url)

            # Write file
            with open(self.img_file_path, 'wb') as f:
                f.write(img.content)

        return self.img_file_path

    def download_video(self):
        '''Download recipe video file video output folder.'''
        # File metadata
        file_ext = self.video_url[self.video_url.find('.', len(self.video_url) - 5):]
        self.video_file_path = output_dir + 'videos/' + self.file_name.replace('.json', file_ext)

        # Check if file exists
        if not os.path.isfile(self.video_file_path):
        
            # Download file
            video = r.get(self.video_url)

            # Write file
            with open(self.video_file_path, 'wb') as f:
                f.write(video.content)

        return self.video_file_path



if __name__ == "__main__":
    # Get list of recipe json files
    recipes = os.listdir(output_dir + 'json/')
    
    # Iterate over recipe json files
    for rfile in recipes:
        # print(rfile)
        recipe = Recipe(rfile)
        print('Downloaded: {}'.format(recipe.download_img()))
        print('Downloaded: {}'.format(recipe.download_video()))
        # break