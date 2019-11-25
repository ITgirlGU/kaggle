import csv
from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn import preprocessing

#初始化处理训练文件
def initialization_train():
    try:
        file=open('train.csv','r')
    except FileNotFoundError:
        print('文件不存在')
    else:
        stus=csv.reader(file)
        array_train=[]
        for stu in stus:
            for i in range(13):
                if stu[i]=='?':
                    stu[i]=ord('?')
            array_train.append(stu)
    return array_train

#初始化处理测试文件
def initialization_test():
    try:
        file=open('test.csv','r')
    except FileNotFoundError:
        print('文件不存在')
    else:
        stus=csv.reader(file)
        array_test=[]
        for stu in stus:
            for i in range(13):
                if stu[i]=='?':
                    stu[i]=ord('?')
            array_test.append(stu)
    return array_test

array_train=initialization_train()  
array_test=initialization_test()


label=[]
data=[]
data_test=[]

for i in range(len(array_train)):
    label.append(array_train[i][13])

for i in range(len(array_train)):
    del array_train[i][13]
    data.append(array_train[i])

for i in range(len(array_test)):
    data_test.append(array_test[i])


data=preprocessing.scale(data)
data_test=preprocessing.scale(data_test)
clf=MLPClassifier(hidden_layer_sizes=(5,2)) 
clf.fit(data,label)



forecast=[]
for i in range(len(data_test)):
    forecast.append(clf.predict([data_test[i]])[0])

number=len(forecast)



rows_first=['id','y']
rows=np.array([[0,0]]*number)

for i in range(number):
    rows[i][0]=i+1
    rows[i][1]=forecast[i]

with open('sample-test.csv','w',newline='') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow(rows_first)
    for row in rows:
        writer.writerow(row)
csv_file.close()