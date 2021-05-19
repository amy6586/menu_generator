import json
import csv

with open('/Users/amyraygada/menu_generator/menu_generator/raw_data/2021-04-26_recipes_random.json', 'r') as handle:
    parsed = json.load(handle)

# appends

csvfile = open('formatted_csv/recipes.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

for keys in parsed['recipes']:
		csvwriter.writerow([keys['id'], \
								keys['title'], \
								keys['servings'], \
								keys['readyInMinutes'], \
								keys['pricePerServing'], \
								keys['spoonacularSourceUrl'], \
								keys['summary'], \
								keys['instructions']])
csvfile.close()