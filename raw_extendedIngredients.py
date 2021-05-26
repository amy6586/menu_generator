import json
import csv

with open('raw_data/merged.json') as f:
    data = json.loads(f.read())

# appends

csvfile = open('formatted_csv/extendedIngredients.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, delimiter=',', quotechar='\001', quoting=csv.QUOTE_MINIMAL)

for item in data:
    for recipe in item['recipes']:
        id = recipe['id']

        for ingredient in recipe['extendedIngredients']:
            csvwriter.writerow([id,
				ingredient['id'],
				ingredient['originalString']])
# add all other columns you need

csvfile.close()