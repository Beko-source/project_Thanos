import os
import random

directory = r"C:\Users\pc\Desktop\ASSIG_4\Universe_2"

files_in_directory = os.listdir( directory )
files_in_directory=( random.sample ( files_in_directory , 25 ) )
filtered_files = [file for file in files_in_directory if file.endswith(".png")]
for file in filtered_files:
    path_to_file = os.path.join ( directory , file )
    os.remove( path_to_file )