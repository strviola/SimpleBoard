'''
Created on 2013/09/09

@author: SuzukiRyota
'''


import csv
import os
import sys
import math


# if DEBUG == True: use CSV file for test file
DEBUG = False


if DEBUG:
    SAVE_PATH = os.getcwd() + '/test.csv'
else:
    SAVE_PATH = os.getcwd() + '/save.csv'


# CSV In-Out Utility functions
def stack(var_name, value):
    print('save to ' + var_name)
    writer = csv.writer(open(SAVE_PATH, 'a'))
    writer.writerow([var_name, value])


def read_name(var_name):
    try:
        csv_file = open(SAVE_PATH, 'r')
    except IOError:  # first time access
        f = open(SAVE_PATH, 'w')
        f.close()
        csv_file = open(SAVE_PATH, 'r')
    
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
    f = open(SAVE_PATH, 'w')
    f.close()


def dump():
    try:
        f = open(SAVE_PATH, 'r')
    except IOError:
        print('No data.')
        sys.exit()

    for line in f.readlines():
        print(line)


def read_database(Model, attr_name, var_name):
    '''
    read all data from given model with given variable name
    '''
    for m in Model.objects.all():
        stack(var_name, getattr(m, attr_name))


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
    stack(name, 10)
    stack(name, 1000)
    
    for line in read_name(name):
        print(name + ', ' + line)
    
    int_list = [int(i) for i in read_name(name)]
    
    m = mean(int_list)
    v = variance(int_list)
    d = deviation(int_list)
    
    print('m: %f, v: %f, d: %f' % (m, v, d))
    
    # tchevishev inequality
    t = 500
    if t <= d:
        print('WARNING: This threshold will not make sense')
    p = v / (t * t)
    print('probability: %f' % p)
