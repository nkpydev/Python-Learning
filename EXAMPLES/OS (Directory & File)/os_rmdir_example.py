# NOTE: only empty directory can be removed by this method.

import os

target_dir = 'unwanted'

os.rmdir(target_dir)

# NOTE: if you want to remove all files inside a non-empty directory and then delete the directory, use this:

import shutil

shutil.rmtree(target_dir)