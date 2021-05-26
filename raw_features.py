import json
import csv


with open('raw_data/merged.json') as f:
    data = json.loads(f.read())

csvfile = open('formatted_csv/features.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

for item in data:
    for recipe in item['recipes']:
        id = recipe['id']
        vegan = recipe['vegan']
        vegetarian = recipe['vegetarian']
        glutenFree = recipe['glutenFree']
        dairyFree = recipe['dairyFree']

        csvwriter.writerow([id,
							vegan,
							vegetarian,
							glutenFree,
							dairyFree,
							','.join(recipe['cuisines']),
							','.join(recipe['dishTypes']),
							','.join(recipe['diets'])])

csvfile.close()