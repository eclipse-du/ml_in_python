#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com
import random
import os

def create_data():
    """
    Description:
    create data using uniform distribution,
    with 0.2 filpper error
    ****************************************
    Parameters:
    None
    ****************************************
    Return:
    data:data in the type of List
    """
    data=[]
    for i in xrange(0,20):
        x = random.uniform(-1,1)
        if x>=0:
            y=1
        else:
            y=-1
        if(random.random()<0.2):
            y*=-1
        data.append([x,y])
    return data

if __name__ == '__main__':
    size = 5000
    if not os.path.isdir("data"):
        os.mkdir("data")  
    for i in xrange(0,size):
        data = create_data()
        file_object = open('data/rawdata_ds_'+str(i)+'.txt', 'w')
        for (a,b) in data:
            k= str(a)+"," + str(b)
            file_object.write(k+"\n")
        file_object.close()