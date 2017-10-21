#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
data_dict.pop('TOTAL', 0)  # removing outlier
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)



### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# print data_dict
## find maximum value
# print data.max()
for person in data_dict:
    if data_dict[person]['salary'] == 97343619.0 or data_dict[person]['bonus'] == 97343619:
        print "What's the name of the dictionary key of this outlier data point?", person


for person in data_dict:
    if (data_dict[person]['salary']>1000000 and data_dict[person]['bonus']>=5000000 and data_dict[person]['salary'] != 'NaN'):
        print "What's the name of the person, who made at least 5 million as bonus and salary of over 1 million?", person
