import os

sep = os.sep

def normalize(path):

    if sep == "\\":
        return path.replace("/", "\\")
    else:
        return path.replace("\\", "/")

def parent(path):

    path = normalize(path)

    if path == sep:
        return sep
    else:
        path = os.path.dirname(path.rstrip(sep))
    if path == "":
        path = sep
    return path

file_dir = parent(os.path.dirname(os.path.abspath(__file__)))

def join(path, name):

    path = normalize(path)
    name = normalize(name)

    if path.endswith(sep):
        return f"{path}{name}"
    else:
        return f"{path}{sep}{name}"

def name(path):

    normalize(path)
    idx = path.rfind(sep)
    return path[idx + 1:]

def convert(path):

    normalize(path)
    return f"{file_dir}{sep}{path}"

if __name__ == "__main__":
    print("this is the aysAPI.")
    print("it is not meant to be run directly.")