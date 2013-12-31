#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com

import os


def load_data(input_file, regex=None):
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
    if regex == None:
        regex = ','
    with open(input_file) as f:
        data = [[float(x) for x in line.strip(' ').strip('\n'
                ).split(regex)] for line in f]
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


def find_median_value_index(list_data, value):
    """
    Description:
    Get given value in list_data 
    return the median one's index
    ****************************************
    Parameters:
    list_data   :data source(list)
    value       :value in data
    ****************************************
    Return:
    index:the median value's index
    """

    count = list_data.count(value)
    count = count / 2 + 1
    step = 1
    for i in xrange(0, len(list_data)):
        if list_data[i] == value:
            if step == count:
                return i
            step += 1


def decisio_stump_single(data):
    """
....Description:
....Create Theta using given data
....****************************************
....Parameters:
....data   :data source(list)
....****************************************
....Return:
....thetas:all theta in the type of List
...."""

    size = len(data)
    data.sort(key=lambda x: x[0])
    thetas = create_Theta(data)
    tmp = [sum([1 for i in xrange(0, size) if data[i][0] < thetas[j]
           and data[i][1] == -1 or data[i][0] > thetas[j]
           and data[i][1] == 1]) for j in xrange(0, len(thetas))]
    t_max = max(tmp)
    t_min = min(tmp)
    if t_max >= size - t_min:
        index = find_median_value_index(tmp, t_max)
        return [thetas[index], 1, (size - t_max) / (size * 1.0)]
    else:
        index = find_median_value_index(tmp, t_min)
        return [thetas[index], -1, t_min / size]


def test_single_ds():
    """
    Description:
    Testing my method to implement the
    algorithm of single variable sc
    ****************************************
    Parameters:
    None
    ****************************************
    Return:
    ein   : error in the case of ds
    eout  : error of the real data case
    """

    ein = 0.0
    eout = 0.0
    for data_file in os.listdir('data'):
        data = load_data('data/' + data_file)
        ans = decisio_stump_single(data)
        ein += ans[2]
        eout += 0.3 * ans[1] * (abs(ans[0]) - 1)
    size = len(os.listdir('data'))
    return (ein / size, (eout + size / 2.0) / size)


def test_multi_ds():
    data = load_data('multi_sc_train.txt', ' ')
    for i in data:
        print i


if __name__ == '__main__':
    print test_single_ds()

    # test_multi_ds()
