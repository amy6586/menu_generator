make all: clean

.jq:
	wget https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64
	mv jq-linux64 jq
	chmod 777 jq
	touch $@

.python:
	wget https://www.python.org/ftp/python/3.8.4/Python-3.8.4.tgz
	mv Python-3.8.4.tgz python
	chmod 777 python
	touch $@

psycopg2_Install:
	pip3 install psycopg2-binary
	touch $@

TODAY = $(shell date --date='today' '+%F')

recipes_vegan.json:
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=vegan&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_vegan.json

recipes_vegeterian.json: recipes_vegan.json
	curl "https://api.spoonacular.com/recipes/random?limitLicense=true&tags=vegetarian&number=1&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_vegetarian.json

recipes_meat.json: recipes_vegeterian.json
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=meat&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_meat.json

recipes_fish.json: recipes_meat.json
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=fish&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_fish.json

recipes_chicken.json: recipes_fish.json
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=chicken&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_chicken.json

recipes_dessert.json: recipes_chicken.json
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=dessert&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_dessert.json

recipes_random.json: recipes_dessert.json
	curl "https://api.spoonacular.com/recipes/random?limitLicense=false&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_random.json

raw_extendedIngredients: recipes_random.json
	python3 raw_extendedIngredients.py

raw_features: raw_extendedIngredients
	python3 raw_features.py

raw_recipes: raw_features
	python3 raw_recipes.py

raw_scores: raw_recipes
	python3 raw_scores.py

postgres_script: raw_scores
	python3 RDS-connect.py

clean : postgres_script
	-rm formatted_csv/*.csv
