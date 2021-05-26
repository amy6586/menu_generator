make all: clean

requirements:
	pip install -U -r requirements.txt

TODAY = $(shell date --date='today' '+%F')

recipes_vegan.json: requirements
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

merge_data: recipes_random.json
	jq -s '.' *.json > raw_data/merged.json

raw_extendedIngredients: merge_data
	python3 raw_extendedIngredients.py

raw_features: raw_extendedIngredients
	python3 raw_features.py

raw_recipes: raw_features
	python3 raw_recipes.py

raw_scores: raw_recipes
	python3 raw_scores.py

postgres_script: raw_scores
	python3 RDS-connect.py

gevalidations: postgres_script
	python3 run_pgfinaltable.py

clean : gevalidations
	-rm formatted_csv/*.csv