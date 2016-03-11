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
Output: Estimated probability of each cuisine

Form of Output:
	cuisine_probs should be a dictionary with the keys being cuisines and the 
	values being the probability of them occurring.

	This is an example of what it should look like (all these probabilities are made up):
	cuisine_probs = 
	{u'brazilian': 0.1,
	 u'british': 0.4,
	 u'cajun_creole': 0.2,
	 u'chinese': 0.2,
	 u'filipino': 0.1}

As a sanity check, try to make sure that the sum of the cuisine probabilities is 1.
"""
def get_cuisine_probs(data):
	cuisine_count = {}

	# Calculate number of times each ingredient and cuisine appears in the whole dataset
	for recipe in data:
		cuisine = recipe['cuisine']
		cuisine_count[cuisine] = cuisine_count.get(cuisine, 0) + 1

	# Divide by length of dataset
	cuisine_probs = {cuisine : cuisine_count[cuisine]/float(len(data)) for cuisine in cuisine_count}

	return cuisine_probs

"""
Input: List of recipes
Output: Estimated probability of an ingredient given that the recipe is a particular cuisine

Form of Output:
	ingredient_prob_given_cuisine should be a dictionary with the keys being
	cuisine and the values being dictionaries. Each value dictionary should
	have keys being ingredients and value being the probability of the ingredient
	given that cuisine.

	This is an example of what it should look like (all these probabilities are made up):
	ingredient_prob_given_cuisine = {
	u'vietnamese': {u'low-sodium fat-free chicken broth': 0.1,
					u'sweetened coconut': 0.05,
					u'baking chocolate': 0.0432,
					u'egg roll wrappers': 0.00043,
					u'bottled low sodium salsa': 0.291,
					... }
	u'indian': {u'low-sodium fat-free chicken broth': 0.00123,
					u'sweetened coconut': 0.0432,
					u'baking chocolate': 0.0,
					u'egg roll wrappers': 0.00032,
					u'bottled low sodium salsa': 0.00940,
					... }
	}

	Again, as a sanity check, make sure that the probability of the ingredients sum to 1 
	(or very close to 1, there might be some rounding errors) for each cuisine.
"""
def get_ingredient_prob_given_cuisine(data):
	ingredient_prob_given_cuisine = {}
	
	# Calculate number of times each ingredient occurs for a given cuisine
	for recipe in data:
		cuisine = recipe['cuisine']
		ingredients = recipe['ingredients']
		for ingredient in ingredients:
			ingredient_probs = ingredient_prob_given_cuisine.get(cuisine, {})
			ingredient_probs[ingredient] = ingredient_probs.get(ingredient, 0) + 1
			ingredient_prob_given_cuisine[cuisine] = ingredient_probs

	# Divide by total number of times the cuisine appears
	for cuisine in ingredient_prob_given_cuisine:
		probs = ingredient_prob_given_cuisine[cuisine]
		total = float(sum(probs[ingredient] for ingredient in probs))
		ingredient_prob_given_cuisine[cuisine] = {ingredient : probs[ingredient]/total for ingredient in probs}

	return ingredient_prob_given_cuisine

"""
Input:
	ingredient_list -> the list of ingredients from a new recipe we want to classify
	cuisine_probs -> result of get_cuisine_probs(data)
	ingredient_prob_given_cuisine -> result of get_ingredient_prob_given_cuisine(data)
Output:
	String identifying most probable cuisine for the given ingredient list

We're trying to estimate p(cuisine | ingredients).
	- cuisine_probs contains p(cuisine) for each cuisine
	- ingredient_prob_given_cuisine contains p(ingredient | cuisine) for each ingredient

Using Bayes' Rule:

	p(cuisine | ingredients) = p(ingredients | cuisine)p(cuisine)/p(ingredients)

We're also making the assumption that each ingredient is independent, so this becomes

	p(cuisine | ingredients) = p(ingredient_1 | cuisine)p(ingredient_2 | cuisine)...p(ingredient_n | cuisine)p(cuisine)/p(ingredients)

But since the ingredients are actually given, we can't change the denominator, so all we care about is

	p(ingredient_1 | cuisine)p(ingredient_2 | cuisine)...p(ingredient_n | cuisine)p(cuisine)

Now, all you have to do is iterate over every cuisine and find the max of the above equation, and return the cuisine that corresponds to that.
"""
def get_max_cuisine(ingredient_list, cuisine_probs, ingredient_prob_given_cuisine):
	max_prob = 0
	best_cuisine = None
	# Iterate over every cuisine
	for cuisine in cuisine_probs:
		# Set probability to p(cuisine)
		prob = cuisine_probs[cuisine]
		# Multiply by p(ingredient | cuisine) for each ingredient in ingredient_list
		for ingredient in ingredient_list:
			prob *= ingredient_prob_given_cuisine[cuisine].get(ingredient, 0)
		# Check if new prob is higher
		if prob > max_prob:
			max_prob = prob
			best_cuisine = cuisine
	return best_cuisine

"""
Test your code by running eval_classifier(test_classifier('train.json'))! You'll get a number between 0 and 1 indicating
the percentage of classifications you got correct. I got 0.635 for my classifier.

Output:
	results -> an array of tuples of the form (guessed cuisine, true cuisine) for each recipe in the test set.
"""
def test_classifier(train_file):
	# Load data from training file
	data = load_data(train_file)
	# Split data into training and test set
	train_data = data[:-1000]
	test_data = data[-1000:]
	# Train the classifier
	cuisine_probs = get_cuisine_probs(train_data)
	ingredient_prob_given_cuisine = get_ingredient_prob_given_cuisine(train_data)

	# Test the classifier
	results = []
	for recipe in test_data:
		cuisine = get_max_cuisine(recipe['ingredients'], cuisine_probs, ingredient_prob_given_cuisine)
		results.append((cuisine, recipe['cuisine']))

	return results

"""
Counts the number of tuples that match (where guessed_cuisine == true_cuisine)
"""
def eval_classifier(results):
	return sum(guessed_cuisine == true_cuisine for (guessed_cuisine, true_cuisine) in results)/float(len(results))





