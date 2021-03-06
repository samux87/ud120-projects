#!/usr/bin/python

import matplotlib.pyplot as plt
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

'''
#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################
'''
# Modified by Samuele Buosi
### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

# MAKE IT FASTER!!! using 1% of all data
features_train = features_train[:int(len(features_train)/100)]
labels_train = labels_train[:int(len(labels_train)/100)]


# KNN
from sklearn import neighbors

clf = neighbors.KNeighborsClassifier(n_neighbors=3)

clf.fit(features_train,labels_train)

predkNN = clf.predict(features_test)
print('kNN prediction=',predkNN)
# end KNN

'''
# adaBoost
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Create and fit an AdaBoosted decision tree
clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                         algorithm="SAMME",
                         n_estimators=200)

clf.fit(features_train,labels_train)

predAda = clf.predict(features_test)
print('AdaBoost prediction=',predAda)
# end AdaBoost
'''



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
