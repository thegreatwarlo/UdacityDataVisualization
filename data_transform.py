# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:48:26 2017

@author: 821647
"""

import csv

IN_FILE = "SAN_flight_history.csv"

out_list = []

with open(IN_FILE, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for in_row in reader:
        out_row_arr = []
        out_row_del = []
        for i in range(5):
            out_row_arr[i] = in_row[i]
            out_row_arr[i] = in_row[i]
        
        
        