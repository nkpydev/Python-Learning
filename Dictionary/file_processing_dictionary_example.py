# Read from a text file into Dictionary
# Then write from that Dictionary into a CSV

import csv
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

source_file_name = 'NATOPhoneticAlphabets.txt'
source_file_name_with_path = os.path.join(BASE_DIR, source_file_name)

destination_file_name = 'Result.csv'
destination_file_name_with_path = os.path.join(BASE_DIR, destination_file_name)

intermediate_dict = {}

with open(source_file_name_with_path,'r') as rf:
    for line in rf:
        tmp = line.splitlines()
        x,y = tmp[0].split(',')
        if x not in intermediate_dict:
            intermediate_dict[x] = y
with open(destination_file_name_with_path,'a+',newline='') as wf:
    wf_writer = csv.writer(wf)
    for key,value in intermediate_dict.items():
        wf_writer.writerow([key,value])