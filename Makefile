#all: recipes_vegan.json recipes_vegeterian.json recipes_meat.json recipes_fish.json recipes_chicken.json recipes_dessert.json recipes_random.json

.jq:
	wget https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64
	mv jq-linux64 jq
	chmod 777 jq
	touch $@
#json2csv_installed:
	#pip3 install --user json2csv

#TODAY = $(shell date --date='today' '+%F')

#recipes_vegan.json: jq_installed json2csv_installed
	#curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=vegan&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_vegan.json

#recipes_vegeterian.json:
	#curl "https://api.spoonacular.com/recipes/random?limitLicense=true&tags=vegetarian&number=1&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_vegetarian.json

#recipes_meat.json:
	#curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=meat&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_meat.json

#recipes_fish.json:
	#curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=fish&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_fish.json

#recipes_chicken.json:
	#curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=chicken&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_chicken.json

#recipes_dessert.json:
	#curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=dessert&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_dessert.json

#recipes_random.json:
	#curl "https://api.spoonacular.com/recipes/random?limitLicense=false&number=99&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > raw_data/$(TODAY)_recipes_random.json

recipes.json:
	cat 2021-04-23_recipes_fish.json | jq '.recipes[] | [paths(scalars) as $$path | {"key": $$path | join("_"), "value": getpath($$path)}] | from_entries ' > test1.json

ingredients.json:
	cat 2021-04-23_recipes_fish.json | jq '.recipes[].extendedIngredients[] | [paths(scalars) as $$path | {"key": $$path | join("_"), "value": getpath($$path)}] | from_entries ' > test2.json

instructions.json:
	cat 2021-04-23_recipes_fish.json | jq '.recipes[].analyzedInstructions[] | [paths(scalars) as $$path | {"key": $$path | join("_"), "value": getpath($$path)}] | from_entries ' > test4.json

#another.json:
	#cat 2021-04-23_recipes_fish.json | jq '((.recipes[0] | with_entries(select(.value|scalars))) | keys_unsorted) as $keys | $keys, (.recipes[] | [ .[$keys[]] ]) | ./json2csv' > true.json

another.json:
	cat 2021-04-23_recipes_fish.json | jq '.recipes[0]' > true.json
