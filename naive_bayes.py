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
	for recipe in data:
		cuisine = recipe['cuisine']
		ingredients = recipe['ingredients']
		cuisine_probs[cuisine] = cuisine_probs.get(cuisine, 0) + 1
		for ingredient in ingredients:
			ingredient_probs[ingredient] = ingredient_probs.get(ingredient, 0) + 1

	# Divide by length of dataset
	for ingredient in ingredient_probs:
		ingredient_probs[ingredient] = ingredient_probs[ingredient]/float(len(data))
	for cuisine in cuisine_probs:
		cuisine_probs[cuisine] = cuisine_probs[cuisine]/float(len(data))

	return ingredient_probs, cuisine_probs

def get_prob_cuisine_given_ingredient(data):
	prob_cuisine_given_ingredient = {}

	for recipe in data:
		cuisine = recipe['cuisine']
		ingredients = recipe['ingredients']
		for ingredient in ingredients:
			probs = prob_cuisine_given_ingredient.get(ingredient, {})
			probs[cuisine] = probs.get(cuisine, 0) + 1
			prob_cuisine_given_ingredient[ingredient] = probs

	for ingredient in prob_cuisine_given_ingredient:
		probs = prob_cuisine_given_ingredient[ingredient]
		total = float(sum(probs[cuisine] for cuisine in probs))
		prob_cuisine_given_ingredient[ingredient] = {cuisine : probs[cuisine]/total for cuisine in probs}

	return prob_cuisine_given_ingredient

def get_max_cuisine(ingredient_list, possible_cuisines, ingredient_probs, cuisine_probs, prob_cuisine_given_ingredient):
	max_prob = 0
	best_cuisine = None
	for cuisine in possible_cuisines:
		prob = 1
		for ingredient in ingredient_list:
			if ingredient not in ingredient_probs:
				continue
			prob *= ingredient_probs.get(ingredient, 1)
			prob *= prob_cuisine_given_ingredient[ingredient].get(cuisine, 0)
		prob = prob/cuisine_probs[cuisine]
		if prob > max_prob:
			max_prob = prob
			best_cuisine = cuisine
	return best_cuisine

def run_on_test(train_file, test_file):
	train_data = load_data(train_file)
	test_data = load_data(test_file)
	ingredient_probs, cuisine_probs = get_ingredient_and_cuisine_probs(train_data)
	prob_cuisine_given_ingredient = get_prob_cuisine_given_ingredient(train_data)
	possible_cuisines = [cuisine for cuisine in cuisine_probs]

	# Dictionary of results - Form: {id : cuisine}
	result_dict = {}
	for recipe in test_data:
		cuisine = get_max_cuisine(recipe['ingredients'], possible_cuisines, ingredient_probs, cuisine_probs, prob_cuisine_given_ingredient)
		result_dict[recipe['id']] = cuisine

	return result_dict








