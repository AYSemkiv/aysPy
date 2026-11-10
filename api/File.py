import os, shutil
from tkinter import filedialog
from tkinter_unblur import Tk
if __name__ == "__main__":
    import Path
else:
    from . import Path

def read(path):

    with open(Path.convert(path), "r") as file:
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

    if protected(path):
        print("error: the app tried to override a critical file. this is not allowed.")
    else:
        with open(Path.convert(path), "w") as file:
            file.write(content)

def delete(path):

    if protected(path):
        print("error: the app tried to delete a critical file. this is not allowed.")
    else:
        os.remove(Path.convert(path))

def move(path, new_path):

    if protected(path):
        print("error: the app tried to move a critical file. this is not allowed.")
    else:
        shutil.move(Path.convert(path), Path.convert(new_path))

def copy(path, new_path):

    shutil.copy(Path.convert(path), Path.convert(new_path))

def exists(path):
 
    return os.path.isfile(Path.convert(path))

def rename(path, new_name):

    new_path = Path.join(Path.parent(path), new_name)

    if protected(path):
        print("error: the app tried to rename a critical file. this is not allowed.")
    else:
        os.rename(Path.convert(path), new_path)

def size(path):

    return os.path.getsize(Path.convert(path))

def extension(path):

    return os.path.splitext(Path.convert(path))[1]