import json
import csv

with open('raw_data/merged.json') as f:
    data = json.loads(f.read())

# appends

csvfile = open('formatted_csv/recipes.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

for item in data:
    for recipe in item['recipes']:
       csvwriter.writerow([recipe['id'],
								recipe['title'],
								recipe['servings'],
								recipe['readyInMinutes'],
								recipe['pricePerServing'],
								recipe['spoonacularSourceUrl'],
								recipe['summary'],
								recipe['instructions']])
csvfile.close()