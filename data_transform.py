# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:48:26 2017

@author: 821647
"""

import csv

IN_FILE = "SAN_flight_history.csv"
OUT_FILE = "SAN_flight_history_parsed.csv"

<<<<<<< HEAD
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
        
        
        
=======
out_rows = []
with open(IN_FILE, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    
    for row_in in reader:
        out_row_del = []
        out_row_ot = []
        for i in range(5):
            out_row_del.append(row_in[i])
            out_row_ot.append(row_in[i])
        out_row_del.append('Delayed')
        out_row_ot.append('On Time')
        
        out_row_del.append(row_in[8])
        out_row_ot.append(row_in[9])
        out_rows.append(out_row_ot)
        out_rows.append(out_row_del)
        
        
with open(OUT_FILE, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['year', 'month', 'date', 'carrier', 'carrier_name', 'type', 'n_flights'])
    for row in out_rows:
        writer.writerow(row)
>>>>>>> origin/Clemente
