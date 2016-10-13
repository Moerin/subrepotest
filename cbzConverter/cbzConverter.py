#!/usr/bin/env python
# encoding: utf-8
from slugify import slugify

from os import listdir, path, rename
import os
import re
from zipfile import ZipFile

def rename_folders():
    dirs = [d for d in listdir('.') if path.isdir(path.join('.', d))]
    length = range(1, len(dirs)+1)
    name = raw_input("Enter the name of the folder : ")
    if not name:
        name = "Shi_ga_Futari_wo_Wakatsu_Made"
    name = slugify(name)

    print("Rename Folders")
    for x in dirs:
        try:
            a = int(re.search('\d{1,3}', x).group(0))
            new_name = "{}_{:02}".format(name, length.index(a)+1)
            rename(x, new_name)
            rename_files(x, a, new_name)
        except AttributeError as err:
            print(err)

def rename_files(dirs, tome, file_path):

    print("Rename Files")
    for y in listdir(dirs):
        try:
            a = int(re.search('\d{1,3}(?=\.jpg|jpeg)', y).group(0))
            old_name, new_name = path.join(file_path, y), path.join(file_path,
                "tome_{}_{:03}.jpg".format(tome, a))
            rename(old_name, new_name)
            zip_tome(file_path, new_name)
        except AttributeError as err:
            print(y)

def zip_tome(zip_name, file_name):
    with ZipFile('{}.cbz'.format(zip_name), 'a') as myzip:
        print('zip : {}'.format(file_name))
        myzip.write(file_name)


if __name__ == '__main__':
    rename_folders()
