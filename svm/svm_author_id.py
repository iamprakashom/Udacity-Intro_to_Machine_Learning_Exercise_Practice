#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time

from sklearn.metrics import accuracy_score
from sklearn.svm import SVC, LinearSVC

sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# Taking 1% of data
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

# svc = SVC(kernel='linear')
svc = SVC(kernel="rbf", C=10000.0)
t0 = time()
svc.fit(features_train, labels_train)
print "Training time: ", (time() - t0), "s"
t1 = time()
ypred = svc.predict(features_test)
print "Prediction for #10th, #26th and #50th element: ", ypred[10], ypred[26], ypred[50]
print "Prediction time: ", (time() - t1), "s"
print "Accuracy Score", accuracy_score(labels_test, y_pred=ypred)

count = 0
for i in range(len(ypred)):
    if ypred[i] == 1:
        count += 1

print "How many is predicted to be 'Chris' (1)", count


#########################################################


