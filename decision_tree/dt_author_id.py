#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# Modified by Samuele Buosi
#########################################################
### your code goes here ###
from sklearn.tree import tree
from sklearn.metrics import accuracy_score

# MAKE IT FASTER!!! using 1% of all data
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test, labels_test)

# n features question, Modified selector = SelectPercentile(f_classif, percentile=1)
# biggest percentile = more complexity
nfeat=len(features_train[0])
print('nfeatures= ', nfeat)

acc = accuracy_score(pred, labels_test)
print("Accuracy:",acc)

print("FINE")
#########################################################
