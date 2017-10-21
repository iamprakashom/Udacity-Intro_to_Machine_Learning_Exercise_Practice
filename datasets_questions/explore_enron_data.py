#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "How many people are there in the dataset: ", len(enron_data)
print "For each Person, how many features are available: ", len(enron_data['METTS MARK'])
print "Stock Value for James Prentice:", enron_data['PRENTICE JAMES']['total_stock_value']
print "How many email messages do we have from Wesley Colwell to persons of interest? ", enron_data['COLWELL WESLEY']\
    ['from_this_person_to_poi']
print "What is the value of stock options exercised by Jeffrey K Skilling? ", enron_data['SKILLING JEFFREY K']\
    ['exercised_stock_options']
print "Money taken home by Lay: ", enron_data['LAY KENNETH L']['total_payments']
print "Money taken home by Skilling: ", enron_data['SKILLING JEFFREY K']['total_payments']
print "Money taken home by Fastow: ", enron_data['FASTOW ANDREW S']['total_payments']
print "Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of 'total_payments' feature) and how much? ",\
    "\n", "Lay: ", max(enron_data['SKILLING JEFFREY K']['total_payments'], enron_data['FASTOW ANDREW S']['total_payments'], enron_data['LAY KENNETH L']['total_payments'])

counter = 0
print "How many folks in this dataset have a quantified salary?", len([key for key in enron_data if enron_data[key]['salary'] != 'NaN'])
print "What about a known email address? ", len([key for key in enron_data if enron_data[key]['email_address'] != 'NaN'])

num_poi = 0
for key in enron_data:
    if enron_data[key]['poi']==True:
        num_poi += 1
print "How many POIs are available: ", num_poi


## count poi from poi_names.txt file
num_lines = 0
with open("../final_project/poi_names.txt", "r") as f:
    content = f.readlines()
    for line in content:
        # print line.rstrip("\n") if line.startswith("(") else ""
        if line.startswith("("):
            num_lines += 1

print "How many POIs are available: ", num_lines

num_people = len([person for person in enron_data if enron_data[person]['total_payments']=='NaN'])
print "How many people in the E+F dataset (as it currently exists) have 'NaN' for their total payments? What percentage" \
      " of people in the dataset as a whole is this?", num_people, round(100*((num_people)/len(enron_data)), 4)

num_people_poi_nan = len([person for person in enron_data if enron_data[person]['poi'] and \
                          enron_data[person]['total_payments']=='NaN'])
print "How many POIs in the E+F dataset have 'NaN' for their total payments?", num_people_poi_nan
print "What percentage of POI's as a whole is this? ", 100*(num_people_poi_nan/num_poi),"%"


num_people_nan_total_payments = len([person for person in enron_data if enron_data[person]['total_payments']=='NaN'])
print "What is the new number of folks with 'NaN' for total payments?", num_people_nan_total_payments

num_people_nan_total_stock_value = len([person for person in enron_data if enron_data[person]['total_stock_value']=='NaN'])
print "What is the new number of folks with 'NaN' for total stock value?", num_people_nan_total_stock_value/len(enron_data)

