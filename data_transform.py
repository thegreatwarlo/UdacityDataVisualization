# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:48:26 2017

@author: 821647
"""

import csv

IN_FILE = "SAN_flight_history2.csv"
OUT_FILE = "SAN_flight_history_parsed2.csv"

def main():
    out_rows = []
    with open(IN_FILE, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        for row_in in reader:
            out_row_cd = []
            out_row_od = []
            out_row_ot = []
            for i in range(4):
                out_row_cd.append(row_in[i])
                out_row_ot.append(row_in[i])
                out_row_od.append(row_in[i])
            out_row_cd.append('Carrier Delay')
            out_row_od.append('Other Delay')
            out_row_ot.append('On Time')
            
            out_row_cd.append(row_in[8])
            out_row_od.append(row_in[9])
            out_row_ot.append(row_in[10])
            out_rows.append(out_row_cd)
            out_rows.append(out_row_od)
            out_rows.append(out_row_ot)
            
            
    with open(OUT_FILE, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Year', 'Month', 'Carrier', 'Carrier Name',
                         'Type', 'Number of Flights'])
        for row in out_rows:
            writer.writerow(row)

if __name__ == '__main__':
    main()

