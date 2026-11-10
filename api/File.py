import os, shutil
from tkinter import filedialog
from tkinter_unblur import Tk
from . import Path

def read(path):

    path = Path.convert(path)
    with open(path, "r") as file:
        content = file.read()
    return content

def protected(path):

    return path == "ays.py" or path == "api.py"

def get_file(types):

    for key in types:
        types[key] = f"*.{types[key]}"
        
    filetypes = list(types.items())
    path = filedialog.askopenfilename(filetypes=filetypes)
    path = Path.normalize(path)
    return path

def create(path, content):

    path = Path.convert(path)

    if protected(path):
        print("error: the app tried to override a critical file. this is not allowed.")
    else:
        with open(path, "w") as file:
            file.write(content)

def delete(path):

    if protected(path):
        print("error: the app tried to delete a critical file. this is not allowed.")
    else:
        path = Path.convert(path)
        os.remove(path)

def move(path, new_path):

    path = Path.convert(path)
    new_path = Path.convert(new_path)

    if protected(path):
        print("error: the app tried to move a critical file. this is not allowed.")
    else:
        shutil.move(path, new_path)

def copy(path, new_path):

    path = Path.convert(path)
    new_path = Path.convert(new_path)

    shutil.copy(path, new_path)

def exists(path):

    path = Path.convert(path)
    return os.path.isfile(path)

def rename(path, new_name):

    path = Path.convert(path)
    new_path = Path.join(Path.parent(path), new_name)

    if protected(path):
        print("error: the app tried to rename a critical file. this is not allowed.")
    else:
        os.rename(path, new_path)

def size(path):

    path = Path.convert(path)
    return os.path.getsize(path)

def extension(path):

    path = Path.convert(path)
    return os.path.splitext(path)[1]