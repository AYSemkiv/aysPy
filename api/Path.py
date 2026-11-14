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

    file_dir = up(up(__file__))
    normalize(path)
    return f"{file_dir}{sep}{path}"