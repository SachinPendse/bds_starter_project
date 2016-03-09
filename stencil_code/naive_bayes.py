import json

"""
Loads json data into an array
"""
def load_data(filename):
	data = None
	with open(filename) as data_file:
		data = json.load(data_file)
	return data

"""
Input: List of recipes
Output: Estimated probability of each ingredient and cuisine

Form of Output:
	ingredient_probs and cuisine_probs should be a dictionary with the keys being 
	ingredients/cuisines and the values being the probability of them occurring.

	This is an example of what it should look like:
	cuisine_probs = 
	{u'brazilian': 0.1,
	 u'british': 0.4,
	 u'cajun_creole': 0.2,
	 u'chinese': 0.2,
	 u'filipino': 0.1}

As a sanity check, try to make sure that the sum of the cuisine probabilities is 1.
The sum of the ingredient probabilities won't be since there can be many ingredients 
in a single recipe.
"""
def get_ingredient_and_cuisine_probs(data):
	ingredient_probs = {}
	cuisine_probs = {}

	# Calculate number of times each ingredient and cuisine appears in the whole dataset

	# Divide by length of dataset

	return ingredient_probs, cuisine_probs

"""
Input: List of recipes
Output: Estimated probability of a cuisine given that a particular ingredient is in the recipe

Form of Output:
	cuisine_prob_given_ingredient should be a dictionary with the keys being
	ingredients and the values being dictionaries. Each value dictionary should
	have keys being cuisines and value being the probability of the cuisine.

	This is an example of what it should look like:
	cuisine_prob_given_ingredient = {
	u'pita bread rounds': {u'greek': 0.7619047619047619,
  							u'indian': 0.09523809523809523,
						  	u'italian': 0.09523809523809523,
						  	u'mexican': 0.047619047619047616},
 	u'whole wheat spaghetti': {u'chinese': 0.07142857142857142,
						  	u'italian': 0.7857142857142857,
						  	u'japanese': 0.03571428571428571,
						  	u'korean': 0.03571428571428571,
						  	u'mexican': 0.03571428571428571,
						  	u'thai': 0.03571428571428571},
	}

	Again, as a sanity check, make sure that the probability of the cuisines sum to 1 
	for each ingredient.
"""
def get_cuisine_prob_given_ingredient(data):
	cuisine_prob_given_ingredient = {}

	# Calculate number of times each cuisine occurs for a givving ingredient

	# Divide by total number of times the ingredient appears

	return cuisine_prob_given_ingredient

"""
Input:
	ingredient_list -> the list of ingredients from a new recipe we want to classify
	ingredient_probs, cuisine_probs -> result of get_ingredient_and_cuisine_probs(data)
	cuisine_prob_given_ingredient -> result of get_cuisine_prob_given_ingredient(data)
Output:
	String identifying most probable cuisine for the given ingredient list

We're trying to estimate p(ingredient_list | cuisine).
	- ingredient_probs contains p(ingredient) for each ingredient
	- cuisine_probs contains p(cuisine) for each cuisine
	- cuisine_prob_given_ingredient contains p(cuisine | ingredient) for each ingredient

Using Bayes' Rule:

	p(ingredients | cuisine) = p(cuisine | ingredients)p(ingredients)/p(cuisine)

We're also making the assumption that each ingredient is independent, so this becomes

	p(ingredients | cuisine) = p(cuisine | ingredient_1)p(ingredient_1)*p(cuisine | ingredient_2)p(ingredient_2)...p(cuisine | ingredient_n)p(ingredient_n)/p(cuisine)

But since the ingredients are actually given, all we care about is

	p(cuisine | ingredient_1)p(cuisine | ingredient_2)...p(cuisine | ingredient_n)/p(cuisine)

Now, all you have to do is iterate over every cuisine and find the max of the above equation, and return the cuisine that corresponds to that.
"""
def get_max_cuisine(ingredient_list, ingredient_probs, cuisine_probs, cuisine_prob_given_ingredient):
	max_prob = 0
	best_cuisine = None
	# Iterate over every cuisine

		# For each ingredient, multiply by p(cuisine | ingredient)

		# Divide by p(cuisine)

	return best_cuisine

"""
Test your code by running eval_classifier(test_classifier('<path_to>/train.json'))! You'll get a number between 0 and 1 indicating
the percentage of classifications you got correct. I got 0.576 for my classifier.
"""
def test_classifier(train_file):
	data = load_data(train_file)
	train_data = data[:-1000]
	test_data = data[-1000:]
	ingredient_probs, cuisine_probs = get_ingredient_and_cuisine_probs(train_data)
	cuisine_prob_given_ingredient = get_cuisine_prob_given_ingredient(train_data)

	results = []
	for recipe in test_data:
		cuisine = get_max_cuisine(recipe['ingredients'], ingredient_probs, cuisine_probs, cuisine_prob_given_ingredient)
		results.append((cuisine, recipe['cuisine']))

	return results

def eval_classifier(results):
	return sum(a == b for (a, b) in results)/float(len(results))





