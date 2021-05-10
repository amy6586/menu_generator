all: recipes_vegan.json recipes_vegeterian.json recipes_meat.json recipes_fish.json recipes_chicken.json recipes_dessert.json recipes_random.json

jq_installed:
	pip3 install --user jq

json2csv_installed:
	pip3 install --user json2csv

TODAY = $(shell date --date='today' '+%F')

recipes_vegan.json: jq_installed json2csv_installed
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=vegan&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_vegan.json

recipes_vegeterian.json:
	curl "https://api.spoonacular.com/recipes/random?limitLicense=true&tags=vegetarian&number=1&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_vegetarian.json

recipes_meat.json:
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=meat&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_meat.json

recipes_fish.json:
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=fish&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_fish.json

recipes_chicken.json:
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=chicken&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_chicken.json

recipes_dessert.json:
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=dessert&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_dessert.json

recipes_random.json:
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_random.json
