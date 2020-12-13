from sklearn.neighbors import KNeighborsClassifier
import numpy as np
# dataset
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target =  [0, 0, 0, 1, 1, 1]
# fit a k-nearest neighbor model to the data
K = 3
model = KNeighborsClassifier(algorithm='auto', n_neighbors = K, metric='euclidean')
model.fit(X, target)
print(model)
# make predictions
print( '(-2,-2) is class'),
print( model.predict([[-2,-2]]) )
print( '(1,3) is class'),
print( model.predict([[1,3]]) )