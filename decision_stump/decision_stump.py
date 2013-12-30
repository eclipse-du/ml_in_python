#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com

import os

def load_data(input_file):
    """
    Description:
    load from input_file,spliting with ','
    take it into array
    ****************************************
    Parameters:
    input_file   :data source
    ****************************************
    Return:
    data:data in the type of List
    """

    data = []
    with open(input_file) as f:
        data = [[float(x) for x in line.strip('\n').split(',')]
                for line in f]
    return data

def create_Theta(data):
	"""
    Description:
    Create Theta using given data
    ****************************************
    Parameters:
    data   :data source(list)
    ****************************************
    Return:
    thetas:all theta in the type of List
    """
	thetas = [data[0][0] - 0.01] + [(data[i][0] + data[i + 1][0]) / 2
                                   for i in range(0, len(data) - 1)] \
        + [data[len(data) - 1][0] + 0.01]
	return thetas

def decisio_stump_simple(data):
	"""
	Description:
	Create Theta using given data
	****************************************
	Parameters:
	data   :data source(list)
	****************************************
	Return:
	thetas:all theta in the type of List
	"""

	size = len(data)    
	data.sort(key=lambda x: x[0])
	thetas = create_Theta(data)
	tmp = [sum([1 for i in xrange(0,size) if data[i][0]<thetas[j] and data[i][1]==-1 or data[i][0]>thetas[j] and data[i][1]==1]) for j in xrange(0,len(thetas)) ]
	t_max = max(tmp)
	t_min = min(tmp)
	if (t_max>=size-t_min):
		return [thetas[tmp.index(t_max)],1,(size-t_max)/(size*1.0)]
	else:
		return [thetas[tmp.index(t_min)],-1,t_min/size]

if __name__ == '__main__':
    #data = load_data('rawdata_ds.txt')
    count = 0.0
    for data_file in os.listdir('data'):
    	data = load_data('data/'+data_file)
    	ans = decisio_stump_simple(data)
        count += ans[2]
    print count/2000.0