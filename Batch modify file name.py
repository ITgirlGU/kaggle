# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:13:27 2019

@author: Lenovo
"""

import os


def chage_name(path):
    file_list = os.listdir(path) # 获取captcha文件
    for file in file_list:
        oldname = path + '/' + file
        num = int(file.split('.')[0])
        if(num>=10000):
            newname = oldname
        elif(num>=1000):
            newname = path + '/0' + file
        elif(num>=100):
            newname = path + '/00' + file
        elif(num>=10):
            newname = path + '/000' + file
        else:
            newname = path + '/0000' + file
        os.rename(oldname,newname)
    
    

chage_name('D:/E 大三上 机器学习框架/雪梨/第三次/test/test')