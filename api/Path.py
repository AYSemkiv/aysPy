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

def join(*items):

    path = ""
    for i, item in enumerate(items):

        path = f"{path}{sep}{item}"

    return path
def name(path):

    normalize(path)
    idx = path.rfind(sep)
    return path[idx + 1:]

def convert(path):

    normalize(path)
    return f"{file_fol}{sep}{path}"