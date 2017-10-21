#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
import numpy as np

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.30, random_state=42)

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)
print "Accuracy: ", accuracy_score(tree.predict(X_test), y_test)
print "How many in tet set predicted as POI: ", len([label for label in y_pred if label == 1])
print "How many people total people are there in test set? ", len(y_pred)

dummy_pred = np.zeros(29)
print "If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be? ", accuracy_score(dummy_pred, y_test)


def calculate_true_positive(true_label, predicted_label):
    """
    Calcualte and return number of true positive
    :param true_label:
    :param predicted_label:
    :return:
    """
    tp = 0
    for i, j in zip(true_label, predicted_label):
        if i == 1 and i == j:
            tp += 1
    return tp


def calculate_true_negative(true_label, predicted_label):
    """
    calculate and return true negative
    :param true_label:
    :param predicted_label:
    :return:
    """
    tn = 0
    for i, j in zip(true_label, predicted_label):
        if i == 0 and i == j:
            tn += 1
    return tn


def calculate_false_positive(true_label, predicted_label):
    """
    calculate and return false positive
    :param true_label:
    :param predicted_label:
    :return:
    """
    fp = 0
    for i, j in zip(true_label, predicted_label):
        if i == 0 and j == 1:
            fp += 1
    return fp


def calculate_false_negative(true_label, predicted_label):
    """
    calculate false negative and return it.
    :param true_label:
    :param predicted_label:
    :return:
    """
    fn = 0
    for i, j in zip(true_label, predicted_label):
        if i == 1 and j == 0:
            fn += 1
    return fn


print "Number of True Positive: ", calculate_true_positive(y_test, y_pred)

print "What is the Precision of POI identifier? ", precision_score(y_test, y_pred)
print "What is the Recall of POI identifier? ", recall_score(y_test, y_pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "How many true positives are there? ", calculate_true_positive(true_labels, predictions)
print "How many true negatives are there? ", calculate_true_negative(true_labels, predictions)
print "How many false positives are there? ", calculate_false_positive(true_labels, predictions)
print "How many false negatives are there? ", calculate_false_negative(true_labels, predictions)
print "What's the precision of this classifier? ", precision_score(true_labels, predictions)
print "What's the recall of this classifier? ", recall_score(true_labels, predictions)
