# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/17 7:11 PM'

from os import chdir
from os import makedirs
from os import removedirs
from os import rename
from os.path import exists
from os.path import pardir
from shutil import copytree
from shutil import move

# create a directory
def create_directory(name):
    if exists(pardir + "\\" + name):
        print('Folder already exists... Cannot Overwrite this')
    else:
        makedirs(pardir + "\\" + name)

# deletes a directory
def delete_directory(name):
    removedirs(name)

# move folder to specific location
# overwrites the file if it already exists
def move_folder(filename, name_dir, folder):
    if not exists(name_dir+":\\" + folder):
        makedirs(name_dir+":\\"+folder)
    move(filename, name_dir+":\\"+folder+"\\")

