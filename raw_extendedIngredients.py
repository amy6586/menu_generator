import json
import csv

with open('menu_generator/raw_data/2021-04-26_recipes_random.json', 'r') as handle:
    parsed = json.load(handle)

# appends

csvfile = open('formatted_csv/extendedIngredients.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, delimiter=',', quotechar='\001', quoting=csv.QUOTE_MINIMAL)

for recipe in parsed['recipes']:
	id = recipe['id']

# start all line with recipe id
	for ingredient in recipe['extendedIngredients']:
		csvwriter.writerow([id, \
			ingredient['id'], \
			ingredient['originalString']])
# add all othet columns you need

csvfile.close()
