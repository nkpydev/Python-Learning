#--- Generic Imports ---#
import os
from os.path import exists
import csv

# Mention File Name here
file_name = 'Expected.csv'

# Path of the Current Working Directory Method 1
path1 = os.path.dirname(os.path.abspath(__file__))

# Path of the Current Working Directory Method 1
path2 = os.getcwd()

# CSV Table Headers Fields - Static Method
header_fields1 = ['ID','Name','Subject','Marks']

# Data Dictionary - to write into csv
data_to_write = {'ID':'007','Name':'James Bond','Subject':'Spying','Marks':'0'}

# CSV Table Headers Fields - Keys from Dict Method
header_fields2 = data_to_write.keys()

with open(path1 + '/' + file_name,'w',newline='') as fp: # Context open # File opend in 'w' mode [write], you can change to 'a' [appened], but in that case you will have make changes to How the header fields are written
    fwriter = csv.DictWriter(fp,fieldnames=header_fields2) # You can change fieldnames = to header_fields1 or headerfields2
    fwriter.writeheader() # Write header
    fwriter.writerow(data_to_write) # Write Rows