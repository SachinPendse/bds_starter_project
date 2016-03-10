# bds_starter_project

### The Goal

Classify the cuisine of a recipe based on its ingredient list.

### Language

The code here is all in Python because Python is great for short projects and data manipulation. We strongly suggest that you use Python because it will make a lot of this easier and because both of us (Sachin and Roshan) know Python well. If you want to use another language, please let us know. Some languages (e.g. C, Java) will make this a lot harder. Other languages (R, Julia) are also great for this kind of project, but since we don't know them very well, we might not be able to help you as much.

### Getting started on a Naive Bayes Classifier

This guide will walk you through how to create your own Naive Bayes Classifier in Python for the recipe data. If you have github, just clone the repository with the following command: `git clone https://github.com/SachinPendse/bds_starter_project.git`. If you don't have github, no problem - you can create one now or download the data from the [Google Drive](www.google.com) and copy the stencil code from the `stencil_code` folder.

##### The Layout

First, let's walk through what's in the repository. The `data` folder contains two files, `train.json` and `test.json`. You'll be working almost exclusively with `train.json`, which has all the training data you need. `test.json` contains a list of recipes without the cuisine identifiers so that you can submit that to Kaggle when you're done with the project and see how you do. 

The `stencil_code` folder contains, as you might expect, the stencil code for how to create a naive bayes classifier. You'll find some helper functions there like `load_data` and `test_classifier`, which will take care of some side things for you. You'll also find method declarations and comments that will guide you on how to create the naive bayes classifier.

Finally, the `example_code` folder contains an implementation of the naive bayes classifier. Since this is not a class, we're giving you all the answers! In order to get the most out of this, however, please try to implement the classifier yourself before looking at the example code for help. But if you're stuck, definitely take a look there to see if you can figure out what's going wrong.

##### Ok, so what does a Naive Bayes Classifier do?

The Naive Bayes Classifier attempts to estimate the following quantity:

$$
best_cuisine = \argmax_{cuisine} p(ingredients | cuisine)
$$