DB_HOST = "menu-generator.cagfzhepmugi.eu-central-1.rds.amazonaws.com"
DB_NAME = "menu_generator"
DB_USER = "postgres"
DB_PASS = "J6dgs9L5oTwAmtmtklPF"
DB_PORT = "5432"

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
	  "price_per_serving" double precision,
	  "spoonacular_source_url" text,
	  "summary" text,
	  "instructions" text
	);
	
	
	CREATE TABLE if not exists  raw_data.raw_ingredientes (
    "recipe_id" integer NOT NULL,
    "ingredients_id" integer,
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

	""")
except:
	print("Table Created")

with open('formatted_csv/extendedIngredients.csv', 'r') as f:
	reader = csv.reader(f, quotechar='\001', delimiter=',',
                     quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
	next(reader) # Skip the header row
	for row in reader:
		cursor.execute(
			"INSERT INTO raw_data.raw_ingredientes VALUES (%s, %s, %s)",
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