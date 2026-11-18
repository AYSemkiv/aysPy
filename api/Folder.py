import os, shutil
from tkinter import filedialog
if __name__ == "__main__":
    import Path, Terminal as t
else:
    from . import Path, Terminal as t

def list_items(path, fil_fol=None):

    folders = os.listdir(Path.convert(path))
    if fil_fol == None:
        fol = None
    else:
        fil_fol = fil_fol.lower().strip()

        if fil_fol == "fil":
            fol = True
        elif fil_fol == "fol":
            fol = False
        elif fil_fol == None:
            fol = None

    final_list = folders.copy()

    if fol == True:
        for i, item in reversed(list(enumerate(folders))):
            if os.path.isfile(Path.convert(item)):
                final_list.pop(i)
    elif fol == False:
        for i, item in reversed(list(enumerate(folders))):
            if exists(item):
                final_list.pop(i)
    elif fol == None:
        pass

    return final_list

def protected(path):

    return path == "apps" or path == "api" or path == f"apps{Path.sep}" or path == f"api{Path.sep}"
    
def get_folder():

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
        shutil.move(Path.convert(path), Path.convert(new_path))

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

def is_empty(path):

    return not os.listdir(Path.convert(path))