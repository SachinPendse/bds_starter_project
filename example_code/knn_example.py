import json
from collections import Counter
"""
Loads json data into an array
"""
def load_data(filename):
	data = None
	with open(filename) as data_file:
		data = json.load(data_file)
	return data

"""
Implements the K-Nearest-Neighbors algorithm. When it takes in a new list of ingredients, it compares that 
list to all other recipes it has seen and counts the number of ingredients they have in common. It then looks 
at the recipes that the new ingredients list has the most in common with, and picks the most common cuisine from 
that set of recipes. 

The reason it's called Nearest Neighbors is basically because its looking for recipes that are 'nearby' - i.e.
have lots of ingredients in common. The K comes from the number of neighbors it looks for. If you set K = 1, it 
only looks at the closest neighbor. If you set K > 1, then it looks at the K closest neighbors picks the cuisine 
that appears most amongst them.
"""
def get_max_cuisine(ingredients_list, data, k):
	scores = []
	for i, recipe in enumerate(data):
		score = sum(1 if ingredient in recipe['ingredients'] else 0 for ingredient in ingredients_list)
		scores.append((score, i))
	scores = sorted(scores)
	indices = [score[1] for score in scores[-k:]]
	top_cuisines = [data[index]['cuisine'] for index in indices]
	counter = Counter(top_cuisines)
	return counter.most_common(1)[0][0]

"""
Turns each list of ingredients into a set to allow for O(1) searching. If you don't know what this means 
or why it works, don't worry about it. All it does is make the get_max_cuisine code run a bit faster.
"""
def make_ingredient_list_into_set(data):
	for recipe in data:
		recipe['ingredients'] = set(recipe['ingredients'])
	return data

"""
Test your code by running eval_classifier(test_classifier('train.json'))! You'll get a number between 0 and 1 indicating
the percentage of classifications you got correct. This works best with K = 6. I get 0.674 for my classifier.
"""
def test_classifier(train_file, k=6):
	data = load_data(train_file)
	train_data = data[:-1000]
	test_data = data[-1000:]

	train_data = make_ingredient_list_into_set(train_data)

	results = []
	for i, recipe in enumerate(test_data):
		cuisine = get_max_cuisine(recipe['ingredients'], train_data, k)
		results.append((cuisine, recipe['cuisine']))

	return results

def eval_classifier(results):
	return sum(a == b for (a, b) in results)/float(len(results))