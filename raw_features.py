import json
import csv
import os
with open('/Users/amyraygada/menu_generator/menu_generator/raw_data/2021-04-26_recipes_random.json', 'r') as handle:
    parsed = json.load(handle)

# appends

csvfile = open('formatted_csv/features.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

for recipe in parsed['recipes']:
	id = recipe['id']
	vegan = recipe['vegan']
	vegetarian = recipe['vegetarian']
	glutenFree = recipe['glutenFree']
	dairyFree = recipe['dairyFree']

# start all line with recipe id
	csvwriter.writerow([id, \
		vegan, \
		vegetarian, \
		glutenFree, \
		dairyFree, \
		','.join(recipe['cuisines']),
		','.join(recipe['dishTypes']),
		','.join(recipe['diets'])])
# add all othet columns you need

csvfile.close()