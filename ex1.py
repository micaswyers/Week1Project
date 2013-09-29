"""Description:
This program sorts text files originally contained in original_files and 
places them in the correct alphabetical directory in path


original_files = name of folder containing text files to be sorted
path = path to the directory containing original_files

"""
import os, shutil
from sys import argv

script, original_files, path = argv


for number in range(97, 123):
    letter = chr(number)

    if not os.path.exists("%s%s" % (path, letter)):
        os.mkdir("%s%s" % (path, letter))

files = os.listdir("%s%s" % (path, original_files))

for file in files:
    first_letter = file[0]
    shutil.move("%s%s/%s" % (path,original_files, file), 
                "%s%s" % (path, first_letter))


