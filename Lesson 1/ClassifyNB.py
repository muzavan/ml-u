def classify(features_train, labels_train):   
    ### your code goes here!
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    ### create classifier
    clf  = GaussianNB()
    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    ### return the fit classifier
    return clf        
    
def accuracy(features_train, labels_train, features_test, labels_test):
	### your code goes here!
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    ### create classifier
    clf  = GaussianNB()
    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    
	### predict test
	pred = clf.predict(features_test)
    
	### test the results of prediction, with actual results
	
	### first, import acuraccy_score from sklearn.metrics
	from sklearn.metrics import acuraccy_score
	
	score = acuraccy_score(pred,labels_test)
	return score 