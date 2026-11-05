<<<<<<< HEAD
import os
import shutil
from tkinter_unblur import Tk
from tkinter import filedialog

root = Tk()
root.withdraw()
file_dir = os.path.dirname(os.path.abspath(__file__))
sep = os.sep

class Path:

    def normalize(path):

        if sep == "\\":
            return path.replace("/", "\\")
        else:
            return path.replace("\\", "/")

    def join(path, name):

        path = Path.normalize(path)
        name = Path.normalize(name)

        if path.endswith(sep):
            return f"{path}{name}"
        else:
            return f"{path}{sep}{name}"

    def parent(path):

        path = Path.normalize(path)

        if path == sep:
            return sep
        else:
            path = os.path.dirname(path.rstrip(sep))
            if path == "":
                path = sep
            return path

    def name(path):

        Path.normalize(path)
        idx = path.rfind(sep)
        return path[idx + 1:]

    def convert(path):

        Path.normalize(path)
        return f"{file_dir}{sep}{path}"


class File:

    def protected(path):

        return path == "ays.py" or path == "api.py"
    
    def open(types):

        for key in types:
            types[key] = f"*.{types[key]}"
        
        filetypes = list(types.items())
        path = filedialog.askopenfilename(parent=root,filetypes=filetypes)
        path = Path.normalize(path)
        return path

    def read(path):

        path = Path.convert(path)
        with open(path, "r") as file:
            content = file.read()
        return content

    def create(path, content):

        path = Path.convert(path)

        if File.protected(path):
            print("error: the app tried to override a critical file. this is not allowed.")
        else:
            with open(path, "w") as file:
                file.write(content)

    def delete(path):

        if File.protected(path):
            print("error: the app tried to delete a critical file. this is not allowed.")
        else:
            path = Path.convert(path)
            os.remove(path)

    def move(path, new_path):

        path = Path.convert(path)
        new_path = Path.convert(new_path)

        if File.protected(path):
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

        if File.protected(path):
            print("error: the app tried to rename a critical file. this is not allowed.")
        else:
            os.rename(path, new_path)

    def size(path):

        path = Path.convert(path)
        return os.path.getsize(path)

    def extension(path):

        path = Path.convert(path)
        return os.path.splitext(path)[1]

class Folder:

    def protected(path):

        return path == "apps"
        
    def open():

        path = filedialog.askdirectory(parent=root)
        path = Path.normalize(path)
        return path

    def create(path):

        path = Path.convert(path)
        os.makedirs(path, exist_ok=True)

    def delete(path):

        if Folder.protected(path):
            print("error: the app tried to delete a critical folder. this is not allowed.")
        else:
            path = Path.convert(path)
            shutil.rmtree(path)

    def move(path, new_path):

        path = Path.convert(path)
        new_path = Path.convert(path)

        if Folder.protected(path):
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

        if Folder.protected(path):
            print("error: the app tried to rename a critical folder. this is not allowed.")
        else:
            os.rename(path, new_path)

    def list(path):

        path = Path.convert(path)
        return os.listdir(path)

    def is_empty(path):

        path = Path.convert(path)
        return not os.listdir(path)

class Terminal:

    def clear():
        os.system("cls")

    def write(text):

        print(text)

    def ask(text):

        return input(f"{text} ").lower().strip()

    def confirm(text):

        text = input(f"Y/N: {text} ")
        if text.lower() == "y":
            return True
        elif text.lower() == "n":
            return False
        else:
            return None

    def error(text):

        print(f"error: {text}")


if __name__ == "__main__":
    print("this is the aysAPI.")
=======
import os
import shutil
from tkinter_unblur import Tk
from tkinter import filedialog

root = Tk()
root.withdraw()
file_dir = os.path.dirname(os.path.abspath(__file__))
sep = os.sep

class Path:

    def normalize(path):

        if sep == "\\":
            return path.replace("/", "\\")
        else:
            return path.replace("\\", "/")

    def join(path, name):

        path = Path.normalize(path)
        name = Path.normalize(name)

        if path.endswith(sep):
            return f"{path}{name}"
        else:
            return f"{path}{sep}{name}"

    def parent(path):

        path = Path.normalize(path)

        if path == sep:
            return sep
        else:
            path = os.path.dirname(path.rstrip(sep))
            if path == "":
                path = sep
            return path

    def name(path):

        Path.normalize(path)
        idx = path.rfind(sep)
        return path[idx + 1:]

    def convert(path):

        Path.normalize(path)
        return f"{file_dir}{sep}{path}"


class File:

    def protected(path):

        return path == "ays.py" or path == "api.py"
    
    def open(types):

        for key in types:
            types[key] = f"*.{types[key]}"
        
        filetypes = list(types.items())
        path = filedialog.askopenfilename(parent=root,filetypes=filetypes)
        path = Path.normalize(path)
        return path

    def read(path):

        path = Path.convert(path)
        with open(path, "r") as file:
            content = file.read()
        return content

    def create(path, content):

        path = Path.convert(path)

        if File.protected(path):
            print("error: the app tried to override a critical file. this is not allowed.")
        else:
            with open(path, "w") as file:
                file.write(content)

    def delete(path):

        if File.protected(path):
            print("error: the app tried to delete a critical file. this is not allowed.")
        else:
            path = Path.convert(path)
            os.remove(path)

    def move(path, new_path):

        path = Path.convert(path)
        new_path = Path.convert(new_path)

        if File.protected(path):
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

        if File.protected(path):
            print("error: the app tried to rename a critical file. this is not allowed.")
        else:
            os.rename(path, new_path)

    def size(path):

        path = Path.convert(path)
        return os.path.getsize(path)

    def extension(path):

        path = Path.convert(path)
        return os.path.splitext(path)[1]

class Folder:

    def protected(path):

        return path == "apps"
        
    def open():

        path = filedialog.askdirectory(parent=root)
        path = Path.normalize(path)
        return path

    def create(path):

        path = Path.convert(path)
        os.makedirs(path, exist_ok=True)

    def delete(path):

        if Folder.protected(path):
            print("error: the app tried to delete a critical folder. this is not allowed.")
        else:
            path = Path.convert(path)
            shutil.rmtree(path)

    def move(path, new_path):

        path = Path.convert(path)
        new_path = Path.convert(path)

        if Folder.protected(path):
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

        if Folder.protected(path):
            print("error: the app tried to rename a critical folder. this is not allowed.")
        else:
            os.rename(path, new_path)

    def list(path):

        path = Path.convert(path)
        return os.listdir(path)

    def is_empty(path):

        path = Path.convert(path)
        return not os.listdir(path)

class Terminal:

    def clear():
        os.system("cls")

    def write(text):

        print(text)

    def ask(text):

        return input(f"{text} ").lower().strip()

    def confirm(text):

        text = input(f"Y/N: {text} ")
        if text.lower() == "y":
            return True
        elif text.lower() == "n":
            return False
        else:
            return None

    def error(text):

        print(f"error: {text}")


if __name__ == "__main__":
    print("this is the aysAPI.")
>>>>>>> 33e71cb6f758a14de1b4912efebce2cbe5ebef24
    print("it is not meant to be run directly.")