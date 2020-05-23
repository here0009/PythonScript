"""
It was used to change the file name to the folder name + file name, 
then copy the file to the rootfolder, delete the original file.
the path is a parameter in sys[1]
"""
import os
import sys


path = '.'

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if root != path: #not in the root dir
            old_file_path = os.path.join(root, name)
            new_name = root[2:] + name #root was like '.\\1\\2\\3', remove the first 2 characters: '.\'
            new_file_path = os.path.join(path, new_name)
            print('{} have been replaced by {}'.format(old_file_path, new_file_path))
            os.rename(old_file_path, new_file_path)
            os.rmdir(root)