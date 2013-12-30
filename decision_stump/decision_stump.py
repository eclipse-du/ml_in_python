#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com


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


if __name__ == '__main__':
    data = load_data('rawdata_ds.txt')
    data.sort(key=lambda x: x[0])
    for (x, y) in data:
        print x, y
