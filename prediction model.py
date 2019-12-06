

import numpy as np
from sklearn import datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import Imputer
import pandas as pd
from sklearn import decomposition

def in_data():
    print("1")
    digit_all = np.loadtxt('123.csv',delimiter=",")
    print("1")
    label_all = np.loadtxt('456.csv',dtype=str,delimiter=",")
    print("1")
    return digit_all,label_all

digit_all,label_all = in_data()

def in_test_data():
    print("1")
    digit = np.loadtxt('测试.csv',delimiter=",")
    
    return digit

digit = in_test_data()


#降维
pca_0 = decomposition.PCA(n_components=25)

all = np.concatenate((digit,digit_all))

all = pca_0.fit_transform(all)


digit_train = all[100000:,:]
label_train = label_all[:]

X_test_pca_0 = all[:100000,:]

knn = KNeighborsClassifier(n_neighbors = 1)

knn.fit(digit_train,label_train)

b = np.array([])
for i in range(0,100000,5):
    iris_predict_y = knn.predict(X_test_pca_0[i:i+5,:])
    c = ''.join(iris_predict_y)
    b = np.append(b,c)
    if(i%1000==0):
        print(i/1000)
        
def save(answer):
    number = np.array(range(0,answer.shape[0]))
    out = np.vstack((number, answer))
    out = out.T
    out_title = np.array(['id','y'])
    import csv
    with open('out.csv','w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(out_title)
        for row in out:
            writer.writerow(row)
    csv_file.close()
save(b)