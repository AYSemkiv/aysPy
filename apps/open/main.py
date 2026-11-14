import json
def main(dictionary):
    import sys
    sys.path.append("../..")
    from api import File as fi, Folder as fol, Terminal as t, Path as p

    work_dir = dictionary["work_dir"]
    app_fil = dictionary["args"]
    
    if isinstance(app_fil, str):
        app_fil = json.loads(app_fil)
    app_fil = app_fil[0]
    if not fol.exists(work_dir):
        t.error("working folder is nonexistent. this is a bug, if you're running it in aysPy.")
        return
    if not fi.exists(app_fil):
        t.error("file doesn't exist.")
        return
    directory = p.join(work_dir, app_fil)
    print(fi.read(directory))

def usage():
    print("usage: open.app [file_name]. note: the working folder matters, it's going to be inserted.")

if __name__ == "__main__":
    print("DEVELOPER MODE ACTIVE")
    print("open")
    usage()
    dictionary = json.loads(input("enter a dictionary: "))
    main(dictionary)