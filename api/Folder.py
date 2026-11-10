import os, shutil
from tkinter import filedialog
from tkinter_unblur import Tk
from . import Path

def protected(path):

    return path == "apps"
    
def get_file():

    path = filedialog.askdirectory()
    return Path.normalize(path)

def create(path):

    os.makedirs(Path.convert(path), exist_ok=True)

def delete(path):

    if protected(path):
        print("error: the app tried to delete a critical folder. this is not allowed.")
    else:
        shutil.rmtree(Path.convert(path))

def move(path, new_path):

    if protected(path):
        print("error: the app tried to move a critical folder. this is not allowed.")
    else:
        shutil.move(Path.convert(path), Path.convert(path))

def copy(path, new_path):

    shutil.copytree(Path.convert(path), Path.convert(new_path))

def exists(path):

    return os.path.isdir(Path.convert(path))

def rename(path, new_name):

    new_path = Path.join(Path.parent(path), new_name)

    if protected(path):
        print("error: the app tried to rename a critical folder. this is not allowed.")
    else:
        os.rename(Path.convert(path), new_path)

def list(path):

    return os.listdir(Path.convert(path))

def is_empty(path):

    return not os.listdir(Path.convert(path))