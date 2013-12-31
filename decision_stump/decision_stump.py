#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com

import os
import numpy as np


def load_data(input_file, regex=','):
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
        data = [[float(x) for x in line.strip(' ').strip('\n'
                ).split(regex)] for line in f]
    return data


def create_Theta(data, variable_index):
    """
    Description:
    Create Theta using given data
    ****************************************
    Parameters:
    data           :data source(list)
    variable_index :give theta in this axix
    ****************************************
    Return:
    thetas:all theta in the type of List
    """

    thetas = [data[0][variable_index] - 0.01] \
        + [(data[i][variable_index] + data[i + 1][variable_index])
           / 2.0 for i in range(0, len(data) - 1)] + [data[len(data)
            - 1][variable_index] + 0.01]
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


def decision_stump(data, variable_index=0):
    """
    Description:
    Create Theta using given data
    ****************************************
    Parameters:
    data           :data source(list)
    variable_index :using this axix of data
    ****************************************
    Return:
    thetas:all theta in the type of List
    """

    size = len(data)
    y_index = len(data[0]) - 1
    data.sort(key=lambda x: x[variable_index])

    thetas = create_Theta(data, variable_index)
    tmp = [sum([1 for i in xrange(0, size) if data[i][variable_index]
           < thetas[j] and data[i][y_index] == -1
           or data[i][variable_index] > thetas[j] and data[i][y_index]
           == 1]) for j in xrange(0, len(thetas))]
    t_max = max(tmp)
    t_min = min(tmp)
    if t_max >= size - t_min:
        index = find_median_value_index(tmp, t_max)
        return [thetas[index], 1, (size - t_max) / (size * 1.0)]
    else:
        index = find_median_value_index(tmp, t_min)
        return [thetas[index], -1, t_min / (size * 1.0)]


def test_single_ds():
    """
    Description:
    Testing my method to implement the
    algorithm of single variable sc
    ****************************************
    Parameters:
    data  :data source(list)
    ****************************************
    Return:
    ein   : error in the case of ds
    eout  : error of the real data case
    """

    ein = 0.0
    eout = 0.0
    for data_file in os.listdir('data'):
        data = load_data('data/' + data_file)
        ans = decision_stump(data)
        ein += ans[2]
        eout += 0.3 * ans[1] * (abs(ans[0]) - 1)
    size = len(os.listdir('data'))
    return (ein / size, (eout + size / 2.0) / size)


def test_multi_ds(data):
    """
    Description:
    Testing my method to implement the
    algorithm of multiply variable sc
    ****************************************
    Parameters:
    data  :data source(list)
    ****************************************
    Return:
    [theta, s, e_in]  : theta,s is the result we test
    index             : decision_stump's variable index
    """

    indexs = len(data[0]) - 1
    ans = np.array([decision_stump(data, i) for i in xrange(0, indexs)])
    error_index = ans.shape[1] - 1
    min_error = ans.min(0)[error_index]
    for i in xrange(0, len(ans)):
        if ans[i][error_index] == min_error:
            step = i
            break
    return (ans[step], step)


def test_error(
    theta,
    s,
    variable_index,
    test_data,
    ):
    """
    Description:
    Testing MVSC given in tets data
    ****************************************
    Parameters:
    theta             : given theta
    s                 : given s
    variable_index    : given index of data
    test_data         : test data
    ****************************************
    Return:
    test_error        : test error of test data
    """

    size = len(test_data)
    y_index = len(data[0]) - 1
    corret = sum([1 for i in xrange(0, size)
                 if test_data[i][variable_index] < theta
                 and test_data[i][y_index] * s == -1
                 or test_data[i][variable_index] > theta
                 and test_data[i][y_index] * s == 1])
    return 1.0 * (size - corret) / size


if __name__ == '__main__':

    # print test_single_ds()
    # test_multi_ds('rawdata_ds.txt')

    data = load_data('multi_sc_train.txt', ' ')
    ([theta, s, e_in], variable_index) = test_multi_ds(data)
    print e_in
    test_data = load_data('multi_sc_test.txt', ' ')
    print test_error(theta, s, variable_index, test_data)
