import numpy as np
import csv

def sigmoid(z):
    return 1/(1+np.exp(-z))   #exp(-z)  e的-z次方

#获取训练集文件中的所有数据
def init_data():
    data=np.loadtxt('HTRU_2_train.csv',delimiter=',')
    row,width=np.shape(data)
    target=data[:,-1]
    data_1=data[:,0:-1]     
    dataIn=np.insert(data_1,0,1,axis=1)
    return dataIn,target

#梯度下降
def grad_descent(dataMatIn, classLabels):
    #将类别与特征值变成矩阵
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()#转置
    row1,width1=np.shape(dataMatrix)#大小
    #随意生成一个3维向量
    weights=np.ones((width1, 1))
    alpha = 0.001#学习率
    maxCycle = 600#指定次数
    
    for i in range (maxCycle):
        #逻辑回归的预测函数
        h = sigmoid (dataMatrix * weights)
        #根据梯度下降原理，要求代价函数的最小值
        #根据矩阵相乘求得m个样本的偏导数之和
        weights = weights-alpha*dataMatrix.transpose()*(h-labelMat)
    #最终确定的参数
    return weights

#可视化
    '''
def visualization(weights):
    #画图
    data1_x=data[target==0,0]
    data1_y=data[target==0,1]
    data2_x=data[target==1,0]
    data2_y=data[target==1,1]
    
    #可视化逻辑回归
    x=np.arange(3,9,1)
    y=-(weights[0,0]+weights[1,0]*x)/weights[2,0]
    plt.scatter(data1_x,data1_y,label='category is 0',c='b')
    plt.scatter(data2_x,data2_y,label='category is 1',c='r')
    plt.plot(x,y,c='g')
    plt.legend()
    plt.show()

'''
dataIn,target=init_data()
weights=grad_descent(dataIn,target)
#读取测试集文件中的数据
test=np.loadtxt('HTRU_2_test.csv',delimiter=',')
number,width2=np.shape(test)
text_1=[0]*number
for i in range(number):
    if(sigmoid(np.insert(test[i],0,1)*weights)>0.5):
        text_1[i]=1
    else:
        text_1[i]=0

print(number)
rows_first=['id','y']
rows=np.array([[0,0]]*number)
for i in range(number):
    rows[i][0]=i+1
    rows[i][1]=text_1[i]
print(rows)
with open('test.csv','w',newline='') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow(rows_first)
    for row in rows:
        writer.writerow(row)
csv_file.close()
with open('test.csv','r') as read_file:
    reader=csv.reader(read_file)
    print([row for row in reader])





