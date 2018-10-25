#!/usr/bin/python

class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def read(self, size):
        return self.fileobj.read(size).encode()
    def readline(self, size=-1):
        return self.fileobj.readline(size).encode()

import pickle
import sys
import matplotlib.pyplot

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( StrToBytes(open("../final_project/final_project_dataset.pkl", "r") ))
features = ["salary", "bonus"]
# remove the outlier
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)


### your code below
maxSal = 0
maxBon = 0
for point in data:
    salary = point[0]
    bonus = point[1]
    if salary > maxSal:
        maxSal = salary
        macBon = bonus
    matplotlib.pyplot.scatter( salary, bonus )

print ("salary and bonus", maxSal, maxBon)
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
