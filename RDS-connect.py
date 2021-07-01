DB_HOST = "***********"
DB_NAME = "menu_generator"
DB_USER = "postgres"
DB_PASS = "*********"
DB_PORT = "********"

import psycopg2
import psycopg2.extras
import csv

try:
	conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port = DB_PORT)
	print("Connection Succesful")
except:
    print("Connection Failed")


cursor = conn.cursor()

try:
	cursor.execute("""CREATE TABLE if not exists raw_data.raw_recipes (
	  "recipe_id" integer NOT NULL,
	  "title" text,
	  "servings" integer,
	  "ready_in_minutes" integer,
	  "price_per_serving" decimal,
	  "spoonacular_source_url" text,
	  "summary" text,
	  "instructions" text
	);
	
	
	CREATE TABLE if not exists  raw_data.raw_ingredients (
    "recipe_id" integer NOT NULL,
    "ingredients_id" text,
    "ingredients" text
);

CREATE TABLE if not exists  raw_data.raw_scores (
    "recipe_id" integer NOT NULL,
	"very_healthy" text,
	"cheap" text,
	"very_popular" text,
	"aggregate_likes" integer,
	"sustainable" text,
	"spoonacular_score" integer,
	"health_score" integer
);

CREATE TABLE if not exists  raw_data.raw_features (
    "recipe_id" integer NOT NULL,
    "vegan" text,
    "vegetarian" text,
	"gluten_free" text,
	"dairy_free" text,
	"cuisines" text,
	"dish_types" text,
	"diets" text
);

CREATE TABLE if not exists raw_data.raw_nutrition as
	with summary as(SELECT 
                recipe_id, summary
				from raw_data.raw_recipes),
	extracted as(SELECT recipe_id,Regexp_matches(summary, '\>[^<]*fat') AS fat, 
               Regexp_matches(summary, '\>[^<]*protein')  AS protein, 
               Regexp_matches(summary, '\>[^<]*calories') AS calories 
        		from summary),
	transformation as(select recipe_id,
				cast(protein as text),
				cast(fat as text),
				cast(calories as text)
				from extracted),
	finale as(select recipe_id, trim('{">}' from fat) as fat,
			trim('{">}' from protein) as protein, 
			cast(trim('{"> calories}' from calories)as integer) as calories from transformation)
	select * from finale;
	
CREATE TABLE if not exists raw_data.final_data (
	recipe_id integer, 
	title text, 
	servings integer,
	ready_in_minutes integer,
	instructions text,
	fat text, 
	protein text, 
	calories text,
	cuisines text, 
	diets text,
	dish_types text,
	very_healthy text,
	very_popular text, 
	health_score integer);

INSERT INTO raw_data.final_data (recipe_id, title, servings,ready_in_minutes,instructions, fat, protein, calories, cuisines, diets,dish_types, very_healthy,very_popular, health_score)
	Select distinct(r.recipe_id), r.title, r.servings,r.ready_in_minutes,
	r.instructions,
	n.fat, n.protein, n.calories,
	f.cuisines, f.diets,f.dish_types,
	s.very_healthy, s.very_popular, s.health_score
	from raw_data.raw_recipes as r
	join raw_data.raw_nutrition as n
	on r.recipe_id = n.recipe_id
	join raw_data.raw_features as f
	on r.recipe_id = f.recipe_id
	join raw_data.raw_scores as s
	on r.recipe_id = s.recipe_id;
""")

except:
	print("Table NOT Created")

with open('formatted_csv/extendedIngredients.csv', 'r') as f:
	reader = csv.reader(f, quotechar='\001', delimiter=',',
                     quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
	next(reader) # Skip the header row
	for row in reader:
		cursor.execute(
			"INSERT INTO raw_data.raw_ingredients VALUES (%s, %s, %s)",
			row)

with open('formatted_csv/scores.csv', 'r') as f:
	reader = csv.reader(f, quotechar='\001', delimiter=',',
                     quoting=csv.QUOTE_ALL, skipinitialspace=True)
	next(reader) # Skip the header row
	for row in reader:
		cursor.execute(
			"INSERT INTO raw_data.raw_scores VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
			row)

with open('formatted_csv/recipes.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		cursor.execute(
			"INSERT INTO raw_data.raw_recipes VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
			row)

with open('formatted_csv/features.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader) # Skip the header row
	for row in reader:
		cursor.execute(
			"INSERT INTO raw_data.raw_features VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
			row)

conn.commit()
cursor.close()
conn.close()
