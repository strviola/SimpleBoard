# -*- coding: utf-8 -*-

'''
Created on 2013/09/09

@author: SuzukiRyota
'''


import csv
import os
import sys
import math

# if DEBUG == True: use CSV file for test file
DEBUG = True


if DEBUG:
    SAVE_PATH = os.getcwd() + '/test.csv'
else:
    SAVE_PATH = os.getcwd() + '/save.csv'


# CSV In-Out Utility functions
def stack(var_name, value):
    print('save to ' + var_name)
    writer = csv.writer(open(SAVE_PATH, 'ab'))
    writer.writerow([var_name, value])


def read_name(var_name):
    try:
        csv_file = open(SAVE_PATH, 'rb')
    except IOError:  # first time access
        f = open(SAVE_PATH, 'wb')
        f.close()
        csv_file = open(SAVE_PATH, 'rb')
    
    reader = csv.reader(csv_file)
    result_list = []
    for line in reader:
        if line[0] == var_name:
            result_list.append(line[1])
    
    return result_list


def reset():
    print('CAUTHION: This method will reset all stacked data!')
    print('Are you sure? (y/n)')
    if input().startswith('y'):
        _hard_reset()


def _hard_reset():
    f = open(SAVE_PATH, 'wb')
    f.close()


def dump():
    try:
        f = open(SAVE_PATH, 'rb')
    except IOError:
        print('No data.')
        sys.exit()

    for line in f.readlines():
        print(line)


# Statistics functions
def mean(int_list):
    return sum(int_list) / len(int_list)


def variance(int_list):
    m = mean(int_list)
    sq_list = [pow(x - m, 2) for x in int_list]
    return mean(sq_list)


def deviation(int_list):
    return math.sqrt(variance(int_list))
    

if __name__ == '__main__':
    print('Hello CSV backends')
    _hard_reset()
    
    name = 'FIRST_TEST'
    
    stack(name, 10)
    stack(name, 10)
    stack(name, 11)
    stack(name, 10)
    
    for line in read_name(name):
        print(name + ', ' + line)
    
    int_list = [int(i) for i in read_name(name)]
    
    print(mean(int_list))
    print(variance(int_list))
