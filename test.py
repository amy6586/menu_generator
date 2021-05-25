import json
from pprint import pprint
import csv

with open('raw_data/merged.json') as f:
	data = json.loads("[" +
					  f.read().replace("}\n{", "},\n{") +
					  "]") #extra code addded by me to format the json as expected

	#pprint(data)

csvfile = open('formatted_csv/test.csv', 'a', newline='')
csvwriter = csv.writer(csvfile, delimiter=',', quotechar='\001', quoting=csv.QUOTE_MINIMAL)

#original code from you:

''''for keys in parsed['recipes']:
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

csvfile.close()'''''

for n in range(len(data)): #---> my changes but still giving the same issue
	for recipe in data[n]['recipes']: #---> my changes but still giving the same issue
		id = recipe[n]['id'] #---> I tried adding and removing the [n] neither way worked
		vegan = recipe['vegan']
		vegetarian = recipe['vegetarian']
		glutenFree = recipe['glutenFree']
		dairyFree = recipe['dairyFree']

	csvwriter.writerow([id, \
						vegan, \
						vegetarian, \
						glutenFree, \
						dairyFree, \
						','.join(recipe['cuisines']), #---> I tried adding and removing the [n] neither way worked
						','.join(recipe['dishTypes']), #---> I tried adding and removing the [n] neither way worked
						','.join(recipe['diets'])]) #---> I tried adding and removing the [n] neither way worked

csvfile.close()
