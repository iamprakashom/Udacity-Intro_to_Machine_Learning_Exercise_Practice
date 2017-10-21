#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

### Support Vector Machine Implementation
# clf1 = SVC(kernel='linear', gamma=10, verbose=True)
# clf1 = SVC(kernel='rbf', gamma='auto', C=5500000, verbose=True)  # With increase in C parameter increases accuracy by minimizing the margin
# distance and thus making less smooth decision boundry.
# clf1 = SVC(kernel='rbf', gamma=1000, verbose=True)
# clf1 = SVC(kernel='rbf', C=10000.0)
# clf1.fit(features_train, labels_train)
# y_pred1 = clf.predict(features_test)
# print "Accuracy Score: ", round(accuracy_score(labels_test, y_pred1), 3)



################################################################################
## KNeighborsClassifier Implementation
print "*"*10, "KNN Implementation", "*"*10
k_score = []
for n in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors=n, weights='distance')
    knn.fit(features_train, labels_train)
    y_pred3 = knn.predict(features_test)
    print "For n = ", n, "Accuracy Score: ", accuracy_score(labels_test, y_pred3)

print


###############################################################################
## Decision Tree Classifier Implementation
print "*"*10, "Decision Tree Implementation", "*"*10
clf2 = DecisionTreeClassifier(min_samples_split=2)
clf21 = DecisionTreeClassifier(min_samples_split=50)


clf2.fit(features_train, labels_train)
clf21.fit(features_train, labels_train)

y_pred2 = clf2.predict(features_test)
y_pred21 = clf21.predict(features_test)

print "Accuracy Score for min_samples_split(2): ", round(accuracy_score(labels_test, y_pred2), 3)
print "Accuracy Score for min_samples_split(50): ", round(accuracy_score(labels_test, y_pred21), 3)


###############################################################################
## Random Forest Classifier Implementation
print "*"*10, "RandomForestClassifier Implementation", "*"*10
for n in range(5, 50):
    rfc = RandomForestClassifier(n_estimators=n, max_features='sqrt', criterion='entropy', random_state=124)
    rfc.fit(features_train, labels_train)
    y_pred4 = rfc.predict(features_test)
    print "for n_estimator: ", n, "Accuracy Score: ", round(accuracy_score(labels_test, y_pred4), 3)
print



###############################################################################
## AdaBoostClassifier Implementation
print "*"*10, "AdaBoostClassifier Implementation", "*"*10

'''The most common algorithm used with AdaBoost are decision trees with one level. Because these trees are so short and only 
contain one decision for classification, they are often called decision stumps.'''
# dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
# dt_stump.fit()
for estimator in range(1, 400):
    adaboost = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1, criterion="gini"), n_estimators=estimator)
    adaboost.fit(features_train, labels_train)
    y_pred5 = adaboost.predict(features_test)
    print "No. of Estimator: ", estimator, "\t", "Accuracy Score: ", round(accuracy_score(labels_test, y_pred5), 4)



try:
    pass
    # prettyPicture(clf1, features_test, labels_test)
except NameError:
    pass
