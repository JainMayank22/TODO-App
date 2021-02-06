#!/usr/bin/env python
# coding: utf-8

# # ML Assignment with extensions such as log probability and nominal attributes.........

# #  Reading .data or .txt file and converting into dataframe for better understanding

# In[95]:


import pandas as pd

read_file = pd.read_csv (r'breast-cancer.data')
#read_file.columns = ['Class','Age','Menopause','tumor-size','inv-nodes','node-caps','deg-malig','breast','breast-quad','irradiat']
read_file.to_csv (r'breast-cancer.csv', index=None)
datasetbc = pd.read_csv('breast-cancer.csv')


# In[96]:


print(datasetbc[:5])


# In[97]:


from csv import reader


def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset
dt = 'breast-cancer.data'
dataset = load_csv(dt)


# In[98]:


print(dataset[0])


# # Nominal Attribute

# In[108]:


from csv import reader

def load_csv(filename):
	file = open(filename, "rt")
	lines = reader(file)
	dataset = list(lines)
	return dataset
 

def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column])
 
# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
 
# Load dataset
filename = 'breast-cancer.data'
dataset = load_csv(filename)
l = len(dataset[0])
print(l)
for i in range(l):
    if i == 6:
        continue
    lookup = str_column_to_int(dataset, i)
for i in range(10):
    str_column_to_float(dataset, i)
print(dataset)


# # Spliting Data by Class

# In[100]:


# Split the dataset by class values
def separate_by_class(dataset):
    separated = dict()
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[0]
        if (class_value not in separated):
            separated[class_value] = list()
        separated[class_value].append(vector)
    return separated
x = separate_by_class(dataset)
print(x)


# #  Implementing Naives Bayes on your selection.

# #  There are two methods you can implement one with log and other without log probability all you have to do is uncomment the return statement of calculate_probability with log return.

# In[1]:


# Naive Bayes 
from csv import reader
from random import seed
from random import randrange
from math import sqrt
from math import exp
from math import pi
import math



# Implementing k folds
def validation_splits_kfold(dataset, n_folds):
    data_split = list()
    data_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for _ in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(data_copy))
            fold.append(data_copy.pop(index))
        data_split.append(fold)
    return data_split



# Calculate accuracy percentage
def accuracy_check(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


# Numerical Values of the text data
def str_column_to_int(dataset, column):
    c_values = [row[column] for row in dataset]
    unique = set(c_values)
    store = dict()
    for i, value in enumerate(unique):
        store[value] = i
    for row in dataset:
        row[column] = store[row[column]]
    return store






# Evaluate an algorithm using a 10FCV
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = validation_splits_kfold(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_check(actual, predicted)
        scores.append(accuracy)
    return scores

# Split the dataset by class values
def separate_by_class(dataset):
    separated = dict()
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[-1]
        if (class_value not in separated):
            separated[class_value] = list()
        separated[class_value].append(vector)
    return separated


# Loading file
def load_csv(filename):
    file = open(filename, "rt")
    lines = reader(file)
    dataset = list(lines)
    return dataset
 
    
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column])
        

# Calculate the mean of a list of numbers
def mean(numbers):
    return sum(numbers)/float(len(numbers))

# Calculate the standard deviation of a list of numbers
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
    return sqrt(variance)



# Calculate the Gaussian probability distribution function for x
def calculate_probability(x, mean, stdev):
    if(stdev == 0.0):
        stdev = 0.1  
    try:
        exponent =exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    except ZeroDivisionError:
        exponent = 0
    return (1 / (sqrt(2 * pi) * stdev)) * exponent
#     return (math.log(exponent)-math.log((sqrt(2 * pi) * stdev))) # log probability for better results



# Predict the class for a given row
def predict(summaries, row):
    probabilities = calculate_class_probabilities(summaries, row)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label

# Naive Bayes Algorithm
def naive_bayes(train, test):
    summarize = summarize_by_class(train)
    predictions = list()
    for row in test:
        output = predict(summarize, row)
        predictions.append(output)
    return(predictions)


    
# Calculate the mean, stdev and count
def summarize_dataset(dataset):
    summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
    del(summaries[-1])
    return summaries

# Split and calculate statistics for each row
def summarize_by_class(dataset):
    separated = separate_by_class(dataset)
    summaries = dict()
    for class_value, rows in separated.items():
        summaries[class_value] = summarize_dataset(rows)
    return summaries        

# Calculate the probabilities
def calculate_class_probabilities(summaries, row):
    total_rows = sum([summaries[label][0][2] for label in summaries])
    probabilities = dict()
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
        for i in range(len(class_summaries)):
            mean, stdev, _ = class_summaries[i]
            probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
    return probabilities


# Test Naive Bayes on different Dataset 
print("Select your choice from the following")
print("1) Hayes-Roth Dataset")
print("2) Car Dataset")
print("3) Breast Cancer Dataset")
print("4) Exit")

a = input()
 
if int(a)>0 and int(a)<=4:
    if int(a) == 1:
        # Load dataset
        filename = 'hayes-roth.data'
        dataset = load_csv(filename)
        r = len(dataset[0])
        # convert string columns to float
        for i in range(r):
            str_column_to_float(dataset, i)
        print(dataset)
    elif int(a) == 2:
        # Load dataset
        filename = 'car.data'
        dataset = load_csv(filename)
        r = len(dataset[0])
        # convert class column to int
        for i in range(r):
            store = str_column_to_int(dataset, i)
        # convert string columns to float
        for i in range(r):
            str_column_to_float(dataset, i)
#             print(dataset)
    elif int(a) == 3:
        # Load dataset
        filename = 'breast-cancer.data'
        dataset = load_csv(filename)
        r = len(dataset[0])
        # convert class column to int
        for i in range(r):
            if i == 6:
                continue
            store = str_column_to_int(dataset, i)
        # convert string columns to float
        for i in range(r):
            str_column_to_float(dataset, i)
        print(dataset)
    elif int(a) == 4:
        exit()
        
else:
    print("Please select proper input from 1 to 3")
    exit()

seed(1)
# print(dataset)
n_folds = 10
scores = evaluate_algorithm(dataset, naive_bayes, n_folds)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))


# In[ ]:




