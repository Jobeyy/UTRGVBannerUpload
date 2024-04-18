import numpy as np
import pandas as pd
import csv

def checkZIPCODE(dataset):
    list_of_valid_zips = ["78542", "78541"]
    for row in dataset:
        if(row[4] == 'ZIPCODE'):
            continue
        if(row[4] not in list_of_valid_zips or len(row[0]) == 0):
            row[4] = "78542"
    return dataset
        
    

with open("data.csv", "r") as csvfile:
    
    reader = csv.reader(csvfile)
    rows = list(reader)

    dataset=checkZIPCODE(rows)
    print(dataset)
    



