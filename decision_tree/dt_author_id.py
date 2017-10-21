#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time

import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

sys.path.append("../tools/")
sys.path.append("../choose_your_own/")
from class_vis import prettyPicture
from sklearn.tree import DecisionTreeClassifier
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
print "Number of Feauture: ", len(features_train[0])
clf = DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf.fit(features_train, labels_train)
print "Training Time: ", time() - t0, "s"
t1 = time()
ypred = clf.predict(features_test)
print "Prediction Time: ", time() - t1, "s"
print "Accuracy Score: ", round(accuracy_score(labels_test, ypred), 4)

#########################################################


