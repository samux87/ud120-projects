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
# Modified by Samuele Buosi during the course (lesson 6)

import pickle

class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def read(self, size):
        return self.fileobj.read(size).encode()
    def readline(self, size=-1):
        return self.fileobj.readline(size).encode()

enron_data = pickle.load(StrToBytes(open("../final_project/final_project_dataset.pkl", "r")))
'''
# scorro gli elementi
for item in enron_data:
    print(item)

# seleziono un elemento
print (enron_data["FOY JOE"])
'''
c=0
for person_name in enron_data:
    if enron_data[person_name]["poi"]==1:
        c +=1



print('n data=', len(enron_data), 'n features=',len(enron_data["FOY JOE"]),'n poi=',c,
'JAMES stock=',enron_data["PRENTICE JAMES"]["total_stock_value"],
'Colwell emails to poi=', enron_data["COLWELL WESLEY"]["from_this_person_to_poi"],
'Jeffrey K Skilling =', enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
