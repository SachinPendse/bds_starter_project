# bds_starter_project

### The Goal

Classify the cuisine of a recipe based on its ingredient list. This is from the [What's Cooking? Kaggle Competition](https://www.kaggle.com/c/whats-cooking).

### Language

The code here is all in Python because Python is great for short projects and data manipulation. We strongly suggest that you use Python because it will make a lot of this easier and because both of us (Sachin and Roshan) know Python well. If you want to use another language, please let us know. Some languages (e.g. C, Java) will make this a lot harder. Other languages (R, Julia) are also great for this kind of project, but since we don't know them very well, we might not be able to help you as much.

### Getting started on a Naive Bayes Classifier

This guide will walk you through how to create your own Naive Bayes Classifier in Python for the recipe data. If you have github, just clone the repository with the following command: `git clone https://github.com/SachinPendse/bds_starter_project.git`. If you don't have github, no problem - you can create one now or download the data from the [Google Drive](https://drive.google.com/folderview?id=0B19mMjbIHfJsdUo3blVnY0E4eUk&usp=sharing) and copy the stencil code from the `stencil_code` folder.

##### The Layout

First, let's walk through what's in the repository. The `data` folder contains two files, `train.json` and `test.json`. You'll be working almost exclusively with `train.json`, which has all the training data you need. `test.json` contains a list of recipes without the cuisine identifiers so that you can submit that to Kaggle when you're done with the project and see how you do. 

The `stencil_code` folder contains, as you might expect, the stencil code for how to create a naive bayes classifier. You'll find some helper functions there like `load_data` and `test_classifier`, which will take care of some side things for you. You'll also find method declarations and comments that will guide you on how to create the naive bayes classifier.

Finally, the `example_code` folder contains an implementation of the naive bayes classifier along with a few other things. Since this is not a class, we're giving you all the answers! In order to get the most out of this, however, please try to implement the classifier yourself before looking at the example code for help. But if you're stuck, definitely take a look there to see if you can figure out what's going wrong. The example classifier gets around 63% of the test recipes correct. 

In addition to the naive bayes classifier (located in `naive_bayes_example.py`), there's also a slightly modified naive bayes classifier (`robust_naive_bayes_example.py`) which adds a prior over p(cuisine | ingredient). The prior essentially prevents any cuisine from having zero probability, which helps when you get ingredients that are rare or that have never been seen with a particular cuisine before. This classifier gets around 74% of the test recipes correct. Finally there's a [k-nearest-neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) classifier example, which gets around 67% of the test recipes correct. There's a brief explanation of how this works in the file (it's actually fairly simple).

##### Ok, so what does a Naive Bayes Classifier do?

Note: This is going to be a *brief* overview. Take a look at the [wikipedia article](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) for a better and more in depth explanation.

The Naive Bayes Classifier attempts to estimate the following quantity:

	best_cuisine = argmax_{cuisine} p(cuisine | ingredients)

Ok, so what does that mean? Basically, it's trying to find the cuisine that is most likely given all the ingredients in your list. So for example, if there was pita bread in a recipe, it would assign it a higher probability of being Greek than Indian.

##### How do we estimate that probability?

We apply [Bayes Rule](https://en.wikipedia.org/wiki/Bayes'_rule)! That says that

	p(cuisine | ingredients) = p(ingredients | cuisine)p(cuisine)/p(ingredients)

Then, we make the *naive* assumption that all the ingredients are independent of one another - that is, that seeing one of the ingredients in the recipe tells you no information about the other ingredients. Obviously this makes no sense, but it's a great assumption to make, because it lets us do this

	p(cuisine | ingredients) = p(ingredient_1 | cuisine)p(ingredient_2 | cuisine)...p(ingredient_n | cuisine)p(cuisine)/p(ingredients)

Now, instead of looking at the ingredients all together, we can separate them out and look at them individually, and just multiply the probabilities together.

Also though, if you notice, the denominator is just p(ingredients). But we can't change what the ingredients in the recipe are, only what the cuisine is. So this quantity is constant for a given set of ingredients - which means we can ignore it. That means, all we have to estimate is

	argmax_{cuisine} p(cuisine | ingredients) = argmax_{cuisine} p(ingredient_1 | cuisine)p(ingredient_2 | cuisine)...p(ingredient_n | cuisine)p(cuisine)

##### So how do you actually do any of this?

Well we don't know any of these probabilities. But, we can estimate them from data. The way we do this is to figure out the number of times something appears and divide it by the total size of the dataset. So if you want to know the probability of a cuisine being Greek, we count the number of Greek recipes and divide by the total number of recipes in the dataset.

At this point, you should take a look at the stencil code and try to figure things out. Feel free to email either of us (Sachin Pendse or Roshan Rao) with any questions. This document may also be expanded in the future if we get time to do it.