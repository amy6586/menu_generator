import json
import csv
import glob

'''read_files = glob.glob("raw_data/*.json")
output_list = []

for f in read_files:
	with open(f,"r") as infile:
		output_list.append(json.load(infile))

with open("raw_data/merged.json", "w", encoding="utf8") as outfile:
	json.dump(output_list, outfile)

files=glob.glob("raw_data/*.json")

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('merged.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)'''


with open('raw_data/2021-04-26_recipes_random.json', 'r') as handle:
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