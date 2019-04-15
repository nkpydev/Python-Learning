import os
from os.path import exists

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR,'New')
target_file = os.path.join(TARGET_DIR,'new.txt')

try:
    if not os.path.exists(TARGET_DIR):
        os.mkdir(TARGET_DIR)
    else:
        print('Folder already exists!!')
except OSError:
    print('Error!!')
finally:
    try:
        with open(target_file,'w') as wf:
            wf.write('Hello!')
    except FileNotFoundError:
        print('No such file!')
    finally:
        wf.close()