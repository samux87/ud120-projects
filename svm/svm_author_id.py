#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# MAKE IT FASTER!!! using 1% of all data
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]

# Classifier  playground
#clf = SVC(kernel="linear") # acc 88%
#clf = SVC(kernel="rbf") # acc 61%
clf = SVC(C=10000, kernel="rbf") # acc 89%

clf.fit(features_train,labels_train)

#print("Start prediction")
pred= clf.predict(features_test)

ten = pred[10]
ventisei= pred[26]
cinquanta= pred[50]
print('pred1= %s, pred2=%s, pred3=%s' %(ten, ventisei, cinquanta))
a = 0
b = 0
for i in pred:
    if i == 0:
        a +=1
    else:
        b +=1

print("Sara messages=",a,'Chris messages=',b)

#print("Start accuracy test")
acc = accuracy_score(pred, labels_test)
print("Accuracy:",acc)


print("FINE")
#########################################################
