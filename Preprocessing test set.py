
import numpy as np
import os
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


def read_captcha(path):
    image_label = []
    image_clean = []
    file_list = os.listdir(path) # 获取captcha文件
    n = 0
    for file in file_list:
        n=n+1
        if(n%2000==0):
            print(n)
        image = Image.open(path + '/' + file) # 打开图片
        file_name = file.split(".")[0] #获取文件名，此为图片标签
        image_label.append(file_name)
        image = image.convert('L') # 转换为灰度图像，即RGB通道从3变为1
        im2 = Image.new("L", image.size, 255)
        for y in range(image.size[1]): # 遍历所有像素，将灰度超过阈值的像素转变为255（白）
            for x in range(image.size[0]):
                if -20<=(image.getpixel((x, y))-image.getpixel((0, 0)))<=20:
                    pix = 1
                else:
                    pix = 0
                im2.putpixel((x, y), pix)
                    
        image_clean.append(im2)
        image.close()
    
    return image_label,image_clean

image_label,image_clean = read_captcha('D:/E 大三上 机器学习框架/雪梨/第三次/test/test')


#image_clean = image_transfer(image_array)


image_clean1 = image_clean[:1000]
image_clean2 = image_clean[1000:2000]
image_clean3 = image_clean[2000:3000]
image_clean4 = image_clean[3000:4000]
image_clean5 = image_clean[4000:5000]
image_clean6 = image_clean[5000:6000]
image_clean7 = image_clean[6000:7000]
image_clean8 = image_clean[7000:8000]
image_clean9 = image_clean[8000:9000]
image_clean0 = image_clean[9000:10000]
image_clean11 = image_clean[10000:11000]
image_clean12 = image_clean[11000:12000]
image_clean13 = image_clean[12000:13000]
image_clean14 = image_clean[13000:14000]
image_clean15 = image_clean[14000:15000]
image_clean16 = image_clean[15000:16000]
image_clean17 = image_clean[16000:17000]
image_clean18 = image_clean[17000:18000]
image_clean19 = image_clean[18000:19000]
image_clean10 = image_clean[19000:]

digit1 = np.array([range(900)])
digit2 = np.array([range(900)])
digit3 = np.array([range(900)])
digit4 = np.array([range(900)])
digit5 = np.array([range(900)])
digit6 = np.array([range(900)])
digit7 = np.array([range(900)])
digit8 = np.array([range(900)])
digit9 = np.array([range(900)])
digit0 = np.array([range(900)])
digit11 = np.array([range(900)])
digit12 = np.array([range(900)])
digit13 = np.array([range(900)])
digit14 = np.array([range(900)])
digit15 = np.array([range(900)])
digit16 = np.array([range(900)])
digit17 = np.array([range(900)])
digit18 = np.array([range(900)])
digit19 = np.array([range(900)])
digit10 = np.array([range(900)])

for i in range(1000):
    demo = np.array(image_clean1[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit1 = np.append(digit1,np.array([demo_1]),axis=0)
    digit1 = np.append(digit1,np.array([demo_2]),axis=0)
    digit1 = np.append(digit1,np.array([demo_3]),axis=0)
    digit1 = np.append(digit1,np.array([demo_4]),axis=0)
    digit1 = np.append(digit1,np.array([demo_5]),axis=0)

digit1 = np.delete(digit1,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean2[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit2 = np.append(digit2,np.array([demo_1]),axis=0)
    digit2 = np.append(digit2,np.array([demo_2]),axis=0)
    digit2 = np.append(digit2,np.array([demo_3]),axis=0)
    digit2 = np.append(digit2,np.array([demo_4]),axis=0)
    digit2 = np.append(digit2,np.array([demo_5]),axis=0)
    
digit2 = np.delete(digit2,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean3[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit3 = np.append(digit3,np.array([demo_1]),axis=0)
    digit3 = np.append(digit3,np.array([demo_2]),axis=0)
    digit3 = np.append(digit3,np.array([demo_3]),axis=0)
    digit3 = np.append(digit3,np.array([demo_4]),axis=0)
    digit3 = np.append(digit3,np.array([demo_5]),axis=0)
digit3 = np.delete(digit3,0,axis=0)
print(1)


for i in range(1000):
    demo = np.array(image_clean4[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit4 = np.append(digit4,np.array([demo_1]),axis=0)
    digit4 = np.append(digit4,np.array([demo_2]),axis=0)
    digit4 = np.append(digit4,np.array([demo_3]),axis=0)
    digit4 = np.append(digit4,np.array([demo_4]),axis=0)
    digit4 = np.append(digit4,np.array([demo_5]),axis=0)
digit4 = np.delete(digit4,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean5[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit5 = np.append(digit5,np.array([demo_1]),axis=0)
    digit5 = np.append(digit5,np.array([demo_2]),axis=0)
    digit5 = np.append(digit5,np.array([demo_3]),axis=0)
    digit5 = np.append(digit5,np.array([demo_4]),axis=0)
    digit5 = np.append(digit5,np.array([demo_5]),axis=0)
digit5 = np.delete(digit5,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean6[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit6 = np.append(digit6,np.array([demo_1]),axis=0)
    digit6 = np.append(digit6,np.array([demo_2]),axis=0)
    digit6 = np.append(digit6,np.array([demo_3]),axis=0)
    digit6 = np.append(digit6,np.array([demo_4]),axis=0)
    digit6 = np.append(digit6,np.array([demo_5]),axis=0)
digit6 = np.delete(digit6,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean7[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit7 = np.append(digit7,np.array([demo_1]),axis=0)
    digit7 = np.append(digit7,np.array([demo_2]),axis=0)
    digit7 = np.append(digit7,np.array([demo_3]),axis=0)
    digit7 = np.append(digit7,np.array([demo_4]),axis=0)
    digit7 = np.append(digit7,np.array([demo_5]),axis=0)
digit7 = np.delete(digit7,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean8[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit8 = np.append(digit8,np.array([demo_1]),axis=0)
    digit8 = np.append(digit8,np.array([demo_2]),axis=0)
    digit8 = np.append(digit8,np.array([demo_3]),axis=0)
    digit8 = np.append(digit8,np.array([demo_4]),axis=0)
    digit8 = np.append(digit8,np.array([demo_5]),axis=0)
digit8 = np.delete(digit8,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean9[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit9 = np.append(digit9,np.array([demo_1]),axis=0)
    digit9 = np.append(digit9,np.array([demo_2]),axis=0)
    digit9 = np.append(digit9,np.array([demo_3]),axis=0)
    digit9 = np.append(digit9,np.array([demo_4]),axis=0)
    digit9 = np.append(digit9,np.array([demo_5]),axis=0)
digit9 = np.delete(digit9,0,axis=0)
print(1)


for i in range(1000):
    demo = np.array(image_clean0[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit0 = np.append(digit0,np.array([demo_1]),axis=0)
    digit0 = np.append(digit0,np.array([demo_2]),axis=0)
    digit0 = np.append(digit0,np.array([demo_3]),axis=0)
    digit0 = np.append(digit0,np.array([demo_4]),axis=0)
    digit0 = np.append(digit0,np.array([demo_5]),axis=0)
digit0 = np.delete(digit0,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean11[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit11 = np.append(digit11,np.array([demo_1]),axis=0)
    digit11 = np.append(digit11,np.array([demo_2]),axis=0)
    digit11 = np.append(digit11,np.array([demo_3]),axis=0)
    digit11 = np.append(digit11,np.array([demo_4]),axis=0)
    digit11 = np.append(digit11,np.array([demo_5]),axis=0)
digit11 = np.delete(digit11,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean12[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit12 = np.append(digit12,np.array([demo_1]),axis=0)
    digit12 = np.append(digit12,np.array([demo_2]),axis=0)
    digit12 = np.append(digit12,np.array([demo_3]),axis=0)
    digit12 = np.append(digit12,np.array([demo_4]),axis=0)
    digit12 = np.append(digit12,np.array([demo_5]),axis=0)

digit12 = np.delete(digit12,0,axis=0)
print(1)


for i in range(1000):
    demo = np.array(image_clean13[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit13 = np.append(digit13,np.array([demo_1]),axis=0)
    digit13 = np.append(digit13,np.array([demo_2]),axis=0)
    digit13 = np.append(digit13,np.array([demo_3]),axis=0)
    digit13 = np.append(digit13,np.array([demo_4]),axis=0)
    digit13 = np.append(digit13,np.array([demo_5]),axis=0)
digit13 = np.delete(digit13,0,axis=0)
print(1)



for i in range(1000):
    demo = np.array(image_clean14[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit14 = np.append(digit14,np.array([demo_1]),axis=0)
    digit14 = np.append(digit14,np.array([demo_2]),axis=0)
    digit14 = np.append(digit14,np.array([demo_3]),axis=0)
    digit14 = np.append(digit14,np.array([demo_4]),axis=0)
    digit14 = np.append(digit14,np.array([demo_5]),axis=0)
digit14 = np.delete(digit14,0,axis=0)
print(1)


for i in range(1000):
    demo = np.array(image_clean15[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit15 = np.append(digit15,np.array([demo_1]),axis=0)
    digit15 = np.append(digit15,np.array([demo_2]),axis=0)
    digit15 = np.append(digit15,np.array([demo_3]),axis=0)
    digit15 = np.append(digit15,np.array([demo_4]),axis=0)
    digit15 = np.append(digit15,np.array([demo_5]),axis=0)
digit15 = np.delete(digit15,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean16[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit16 = np.append(digit16,np.array([demo_1]),axis=0)
    digit16 = np.append(digit16,np.array([demo_2]),axis=0)
    digit16 = np.append(digit16,np.array([demo_3]),axis=0)
    digit16 = np.append(digit16,np.array([demo_4]),axis=0)
    digit16 = np.append(digit16,np.array([demo_5]),axis=0)
digit16 = np.delete(digit16,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean17[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit17 = np.append(digit17,np.array([demo_1]),axis=0)
    digit17 = np.append(digit17,np.array([demo_2]),axis=0)
    digit17 = np.append(digit17,np.array([demo_3]),axis=0)
    digit17 = np.append(digit17,np.array([demo_4]),axis=0)
    digit17 = np.append(digit17,np.array([demo_5]),axis=0)
digit17 = np.delete(digit17,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean18[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit18 = np.append(digit18,np.array([demo_1]),axis=0)
    digit18 = np.append(digit18,np.array([demo_2]),axis=0)
    digit18 = np.append(digit18,np.array([demo_3]),axis=0)
    digit18 = np.append(digit18,np.array([demo_4]),axis=0)
    digit18 = np.append(digit18,np.array([demo_5]),axis=0)
digit18 = np.delete(digit18,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean19[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit19 = np.append(digit19,np.array([demo_1]),axis=0)
    digit19 = np.append(digit19,np.array([demo_2]),axis=0)
    digit19 = np.append(digit19,np.array([demo_3]),axis=0)
    digit19 = np.append(digit19,np.array([demo_4]),axis=0)
    digit19 = np.append(digit19,np.array([demo_5]),axis=0)
digit19 = np.delete(digit19,0,axis=0)
print(1)

for i in range(1000):
    demo = np.array(image_clean10[i])
    demo_1 = demo[:,:30].flatten()
    demo_2 = demo[:,30:60].flatten()
    demo_3 = demo[:,60:90].flatten()
    demo_4 = demo[:,90:120].flatten()
    demo_5 = demo[:,120:150].flatten()
    digit10 = np.append(digit10,np.array([demo_1]),axis=0)
    digit10 = np.append(digit10,np.array([demo_2]),axis=0)
    digit10 = np.append(digit10,np.array([demo_3]),axis=0)
    digit10 = np.append(digit10,np.array([demo_4]),axis=0)
    digit10 = np.append(digit10,np.array([demo_5]),axis=0)
digit10 = np.delete(digit10,0,axis=0)
print(1)


digit = np.concatenate((digit1,digit2))
digit = np.concatenate((digit,digit3))
digit = np.concatenate((digit,digit4))
digit = np.concatenate((digit,digit5))
digit = np.concatenate((digit,digit6))
digit = np.concatenate((digit,digit7))
digit = np.concatenate((digit,digit8))
digit = np.concatenate((digit,digit9))
digit = np.concatenate((digit,digit0))
digit = np.concatenate((digit,digit11))
digit = np.concatenate((digit,digit12))
digit = np.concatenate((digit,digit13))
digit = np.concatenate((digit,digit14))
digit = np.concatenate((digit,digit15))
digit = np.concatenate((digit,digit16))
digit = np.concatenate((digit,digit17))
digit = np.concatenate((digit,digit18))
digit = np.concatenate((digit,digit19))
digit = np.concatenate((digit,digit10))




import csv

with open('测试.csv','w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in digit:
        writer.writerow(row)
csv_file.close()



