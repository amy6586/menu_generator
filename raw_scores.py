import json
import csv
import os

with open('/Users/amyraygada/menu_generator/menu_generator/raw_data/2021-04-26_recipes_random.json', 'r') as handle:
    parsed = json.load(handle)

# appends

csvfile = open('formatted_csv/scores.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, delimiter=',', quotechar='\001', quoting=csv.QUOTE_MINIMAL)

for keys in parsed['recipes']:
		csvwriter.writerow([keys['id'], \
								keys['veryHealthy'], \
								keys['cheap'], \
								keys['veryPopular'], \
							    keys['aggregateLikes'], \
								keys['sustainable'], \
								keys['spoonacularScore'], \
								keys['healthScore']])

csvfile.close()