import json
from pprint import pprint
import csv

with open('raw_data/merged.json') as f:
    data = json.loads(f.read())
# data is a list

csvfile = open('formatted_csv/test.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, delimiter=',', quotechar='\001', quoting=csv.QUOTE_MINIMAL)

for item in data:
    for recipe in item['recipes']:
        id = recipe['id']
        vegan = recipe['vegan']
        vegetarian = recipe['vegetarian']
        glutenFree = recipe['glutenFree']
        dairyFree = recipe['dairyFree']

        csvwriter.writerow([id, \
							vegan, \
							vegetarian, \
							glutenFree, \
							dairyFree, \
							','.join(recipe['cuisines']),
							','.join(recipe['dishTypes']),
							','.join(recipe['diets'])])
csvfile.close()
