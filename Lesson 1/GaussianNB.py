import numpy as np

X = np.array([[-1,1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y = np.array(["Class-1","Class-1","Class-1","Class-2","Class-2","Class-2"])

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X,Y)

print(clf.predict([[-0.8,-1]]))