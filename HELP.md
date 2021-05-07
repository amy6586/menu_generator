# Steps to Reproduce

1. Run the Curl Statement:
curl "https://api.spoonacular.com/recipes/random?limitLicense=false&tags=vegan&number=1&apiKey=498c26d092a94f43be3633099e12f569" | jq '.' > recipes_vegan.json

2.
    jq -r '
  	((.recipes[0]
	| with_entries(select(.value|scalars)))
	| keys_unsorted) as $keys
	| $keys,
	(.recipes[] | [ .[$keys[]] ]) | ./json2csv
	' recipes_vegan2.json

**Problem:** I want to have as output a CSV File  that contains all the fields below, this codes is basically separating the data in 2 arrays one with the headers and one with the responses but is misssing the **Extended Ingredients**,  **Measures**, *analyzedInstructions*  because are nested depeer. For reference in this folder you can find sample data:

I have been stuck on this for almost a week :( 

**Desired Fields -->**
    "vegetarian"
    "vegan"
    "glutenFree"
    "dairyFree"
    "veryHealthy"
    "cheap"
    "veryPopular"
    "sustainable"
    "weightWatcherSmartPoints"
    "gaps"
    "lowFodmap"
    "aggregateLikes"
    "spoonacularScore"
    "healthScore"
     "pricePerServing"

        "extendedIngredients"  **----MISSING---**
        "id"
        "image"
        "name"
        "original"
        "amount"
        "unit"
        
          "measures"      **----MISSING---**    
              "metric"
              "amount": 
              "unitShort"
              "unitLong"
         
 "id"
    "title": 
    "readyInMinutes"
    "servings"
    "sourceUrl"
    "image"
    "summary":
    "cuisines":
    "dishTypes": 
    "diets":
    "occasions":
    "instructions"

 "analyzedInstructions":    **----MISSING---**     
"name":
    "steps":          
      "number"
       "step"









