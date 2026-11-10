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
    elif path == "":
        path = sep
        path = os.path.dirname(path.rstrip(sep))
    return path

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

    file_dir = parent(parent(__file__))
    normalize(path)
    return f"{file_dir}{sep}{path}"