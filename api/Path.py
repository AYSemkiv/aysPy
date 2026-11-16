import os
sep = os.sep

def normalize(path):

    if sep == "\\":
        return path.replace("/", "\\")
    else:
        return path.replace("\\", "/")

def up(path):

    path = normalize(path)

    idx = path.rfind(sep)
    path = path[:idx]
    if path == sep:
        path = sep
    elif path == "":
        path = sep

    return path

file_fol = up(up(__file__))

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
    return f"{file_fol}{sep}{path}"