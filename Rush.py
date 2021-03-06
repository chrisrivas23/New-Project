import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import cross_validation
from sklearn import datasets


dataset = pd.read_csv('/Users/chrisrivas/Documents/Datasets/RushDataset.csv', header=None, sep=',')

#coverts dataset into 2d array of values and seperates target column
#[1st to: last rows, and 1st to: 4rth columns ]
samples = dataset.loc[:,1:12].values
targets = dataset[13].values

print(samples)
print(targets)

#training and testing of dataset
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
samples, targets, test_size=0.25, random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

#calculates accuracy of algorithm    
print("Test set score: {:.2f}%".format(np.mean(y_pred == y_test)*100))

#opens new data for algorithm to make classification predictions 
dataset2 = pd.read_csv('/Users/chrisrivas/Documents/Datasets/RushDataset.csv', header=None, sep=',').values

#continues to loop for each sample and their classification prediction
for sample in dataset2:
    
    prediction = knn.predict([sample])
    print("Prediction: {}".format(prediction))
    print('    ')    

    
#other format for predictions: all at a time in array
prediction = knn.predict(dataset2)
print("Prediction: {}".format(prediction))



#X_new = np.array([[5.58,5.08,1.5,5.58]])

#print("Prediction: {}".format(prediction))
#print("Prediction target name: {}".format(
    #iris_dataset['target_names'][prediction]))
   

 #knn.predict(dataset2)



