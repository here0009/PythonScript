# coding: utf-8

# Rename
# Change the name of the files that meet the regex patterns
# if the new filename is already in that directory, move the file to backup folder

import re
import os
import sys


def rename(path):
    counts = 0
    backup_counts = 0
    name_pattern = re.compile(r'\d+\_')  # e.g: 13_foo.py
    backup_folder = path + '\\backup'
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
    for file_name in os.listdir(path):
        if re.match(name_pattern, file_name):
            old_file_name = os.path.join(path, file_name)
            new_file_name = os.path.join(path, re.sub(name_pattern, '', file_name))
            print('{} have been renamed as {}'.format(old_file_name, new_file_name))
            try:
                os.rename(old_file_name, new_file_name)
                counts += 1
            except:
                print('{} already exist, move the renamed file to backup folder'.format(new_file_name))
                backup_name = os.path.join(backup_folder, re.sub(name_pattern, '', file_name))
                backup_counts += 1
                os.rename(old_file_name, backup_name)
    return counts, backup_counts


def main():
    path = sys.argv[1].replace('\\', '\\')
    counts, backup_counts = rename(path)
    print("There are {} files have been renamed, {} files were moved to backup folder".format(counts, backup_counts))


main()