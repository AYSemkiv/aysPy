from . import Path
import os
import shutil
from tkinter_unblur import Tk
from tkinter import filedialog
root = Tk()
root.withdraw()
file_dir = os.path.dirname(os.path.abspath(__file__))

def protected(path):

        return path == "apps"
        
def get_file():

        path = filedialog.askdirectory(parent=root)
        path = Path.normalize(path)
        return path

def create(path):

        path = Path.convert(path)
        os.makedirs(path, exist_ok=True)

def delete(path):

        if protected(path):
            print("error: the app tried to delete a critical folder. this is not allowed.")
        else:
            path = Path.convert(path)
            shutil.rmtree(path)

def move(path, new_path):

        path = Path.convert(path)
        new_path = Path.convert(path)

        if protected(path):
            print("error: the app tried to move a critical folder. this is not allowed.")
        else:
            shutil.move(path, new_path)

def copy(path, new_path):

        path = Path.convert(path)
        new_path = Path.convert(new_path)

        shutil.copytree(path, new_path)

def exists(path):

        path = Path.convert(path)
        return os.path.isdir(path)

def rename(path, new_name):

        path = Path.convert(path)
        new_path = Path.join(Path.parent(path), new_name)

        if protected(path):
            print("error: the app tried to rename a critical folder. this is not allowed.")
        else:
            os.rename(path, new_path)

def list(path):

        path = Path.convert(path)
        return os.listdir(path)

def is_empty(path):

        path = Path.convert(path)
        return not os.listdir(path)

if __name__ == "__main__":
    print("this is the aysAPI.")
    print("it is not meant to be run directly.")