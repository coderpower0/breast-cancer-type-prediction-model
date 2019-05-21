import data
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree, svm, neighbors

X_train, X_test, y_train, y_test = train_test_split(data.X, data.y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)

example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = clf.predict(example_measures)

if prediction == [2]:
    print("benign")
else:
    print("malignant")
