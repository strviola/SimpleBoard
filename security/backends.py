'''
Created on 2013/09/09

@author: SuzukiRyota
'''


import csv
import os


SAVE_PATH = os.getcwd() + 'save.csv'


def stack(var_name, value):
    writer = csv.writer(open(SAVE_PATH, 'a'))
    writer.writerow([var_name, value])


def read_name(var_name):
    try:
        csv_file = open(SAVE_PATH, 'r')
    except IOError:  # first time access
        f = open(SAVE_PATH, 'w')
        f.close()
    
    reader = csv.reader(csv_file)
    result_list = []
    for line in reader:
        if line[0] == var_name:
            result_list.append(line[1])
    
    return result_list
