# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:48:26 2017

@author: 821647
"""

import csv

IN_FILE = "SAN_flight_history.csv"

with open(IN_FILE, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader: