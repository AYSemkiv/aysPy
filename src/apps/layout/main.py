import sys
sys.path.append("../..")

from api import File as fi, Folder as fol, Path as p, Terminal as t


def ask_yes_no(question, default):
    default_text = "Y/n" if default else "y/N"

    while True:
        answer = t.ask(f"{question} ({default_text}):")

        if answer == "":
            return default
        elif answer == "y":
            return True
        elif answer == "n":
            return False


def generate_main(name, settings, selected_api):

    imports = ""

    if selected_api:
        imports = (
            "import sys\n"
            'sys.path.append("../..")\n'
            f"from api import {', '.join(selected_api)}\n\n"
        )

    any_enabled = any(settings.values())
    content = imports

    if settings["args"]:
        content += (
            "def usage():\n"
            f'    print("usage: \'{name}.app <arguments>\'")\n\n'
        )

    if any_enabled:
        content += "def main(dictionary):\n    pass\n\n"
    else:
        content += "def main():\n    pass\n\n"

    content += 'if __name__ == "__main__":\n'
    content += '    print("DEVELOPER MODE ACTIVE")\n'
    content += f'    print("{name}")\n'

    if any_enabled:
        content += "    import json\n"
        content += '    main(json.loads(input("enter a dictionary: ")))\n'
    else:
        content += "    main()\n"

    return content


def main(dictionary):

    t.write("AYS LAYOUT")
    t.write("Create a new aysPy app.\n")

    name = t.ask("app name:")

    if not name.isidentifier():
        t.error("invalid app name.")
        return

    app_dir = p.join("\\apps", name)

    if fol.exists(app_dir):
        t.error("an app with that name already exists.")
        return

    t.write("\nMETADATA")

    settings = {
        "args": ask_yes_no("Arguments", True),
        "file_dir": ask_yes_no("aysPy directory", False),
        "work_dir": ask_yes_no("Working directory", False)
    }

    t.write("\nAYSAPI")

    api_options = [
        ("File", "fi"),
        ("Folder", "fol"),
        ("Path", "p"),
        ("Terminal", "t")
    ]

    selected_api = []

    for api_name, alias in api_options:
        if ask_yes_no(f"Import {api_name}", False):
            selected_api.append(f"{api_name} as {alias}")

    t.write("\nCREATING APP")

    if not fol.create(app_dir):
        t.error("could not create app folder.")
        return

    main_content = generate_main(name, settings, selected_api)

    if not fi.create(p.join(app_dir, "main.py"), main_content):
        t.error("could not create main.py.")
        return

    defaults = {
        "args": True,
        "file_dir": False,
        "work_dir": False
    }

    if settings != defaults:
        metadata = ",".join(
            f"{key}:{int(value)}"
            for key, value in settings.items()
        )

        if not fi.create(p.join(app_dir, "metadata"), metadata):
            t.error("could not create metadata.")
            return

    t.write(f"\nSuccessfully created {name}.app!")


if __name__ == "__main__":
    main({})