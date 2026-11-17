import sys
sys.path.append("../..")
from api import Terminal as t, Path as p, File as fi, Folder as fol
sep = p.sep

apps = []
def app_list():
    global apps
    apps = fol.list_items(f"{sep}apps")
    for i, item in enumerate(apps):
        if fi.exists(item):
            apps.pop(i)

t.clear()
help_list = {
    "help": "the command you're in",
    "info": "list the documentation of an app",
    "ls": "list all of the apps in aysPy",
    "refresh": "refresh the apps list",
    "search": "search apps"
}
help_text = t.make_tables(help_list, "available commands:")

def main():
    app_list()
    print('type "help" for available commands.')
    while True:
        status = loop()
        if status == "exit":
            return

def loop():
    comd = t.ask("appsman>")
    if comd == "":
        comd = " "
        print()
    comds = t.split(comd)
    comd_name = comds[0]

    if comd_name == "exit":

        return "exit"

    if comd_name == "help":

        print(help_text)

    if comd_name == "ls":

        print("apps: \n")
        print("\n".join(apps))
        print()

    if comd_name == "refresh":

        app_list()

    if comd_name == "search":

        if len(comds) == 1:
            print("usage: search [app_name]")
        else:
            matches = []
            keyword = comds[1]
            for i, item in enumerate(apps):
                if keyword in item:
                    matches.append(item)
            table = t.make_table(matches, "found matches:")
            print(table)

    if comd_name == "info":

        if len(comds) == 1:
            print("usage: about [app_name]")
        else:
            app_name = comds[1]
            app_location = p.join("apps", app_name)
            file_location = p.join(app_location, "about")
            if fi.exists(file_location):
                fi.read(file_location)
            elif not fol.exists(app_location):
                t.error("app not found")
            elif not fi.exists(file_location):
                t.warning("app info not found")

if __name__ == "__main__":
    
    print("DEVELOPER MODE ACTIVE")
    print("appsman")
    main()
    t.clear()