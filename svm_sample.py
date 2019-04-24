from sklearn import svm
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
print(clf.fit(X, Y))
dec = clf.decision_function([[1]]) 
print(dec)
print(dec.shape[1])
clf.decision_function_shape = 'ovr'
dec = clf.decision_function([[1]])
print(dec.shape[1])
# lin_clf = svm.LinearSVC()

# clf = svm.SVC(gamma='scale')
# clf.fit(x, y)
# print(clf.predict([[2., 2.]]))
# print(clf.n_support_ )