import json
import csv


with open('raw_data/merged.json') as f:
    data = json.loads(f.read())

# appends
csvfile = open('formatted_csv/scores.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, delimiter=',', quotechar='\001', quoting=csv.QUOTE_MINIMAL)

for item in data:
    for recipe in item['recipes']:
       csvwriter.writerow([recipe['id'],
								recipe['veryHealthy'],
								recipe['cheap'],
								recipe['veryPopular'],
							    recipe['aggregateLikes'],
								recipe['sustainable'],
								recipe['spoonacularScore'],
								recipe['healthScore']])

csvfile.close()