def main(dictionary):
    import sys
    sys.path.append("../..")
    import api
    import zipfile

    install_location = f"{dictionary["file_fol"]}\\apps"

    file_path = api.File.get_file({"aysBundles":"ays"})

    if file_path == "":
        print("error: you cancelled the file selection")
    else:
        with zipfile.ZipFile(file_path, 'r') as archive:
            for name in archive.namelist():
                if name.startswith("aysPy/"):
                    relative_path = name.removeprefix("aysPy/")
                    target_path = api.Path.join(install_location, relative_path)

                if name.endswith({api.Path.sep}):
                    api.Folder.create(relative_path)

                else:
                    api.Folder.create(api.Path.name(relative_path))
                    with archive.open(name) as source, open(target_path, "wb") as target:
                        target.write(source.read())

def usage():
    print("usage: 'import.app'")

if __name__ == "__main__":
    import json

    print("DEVELOPER MODE ACTIVE")
    print("import")
    usage()
    dictionary = json.loads(input("enter a dictionary: "))
    main(dictionary)