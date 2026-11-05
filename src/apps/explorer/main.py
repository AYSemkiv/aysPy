import sys
sys.path.append("../..")
from api import File, Folder, Path, Terminal

def usage():
    Terminal.write(
        "aysExplorer - File Explorer\n\n"
        "Commands:\n"
        "  ls              List directory contents\n"
        "  cd <directory>  Enter a directory\n"
        "  up              Go to parent directory\n"
        "  cls             Clear the terminal\n"
        "  pwd             Show current directory\n"
        "  info <name>     Show file/folder information\n"
        "  help            Show available commands\n"
        "  exit            Exit aysExplorer"
    )


def get_path(work_dir, name):
    return name if name.startswith("\\") else Path.join(work_dir, name)


def list_directory(work_dir):
    contents = Folder.list(work_dir)

    if not contents:
        Terminal.write("This directory is empty.")
        return

    Terminal.write(f"Contents of {work_dir}:")

    for name in contents:
        path = Path.join(work_dir, name)
        kind = "DIR" if Folder.exists(path) else "FILE" if File.exists(path) else "?"

        Terminal.write(f"[{kind}] {name}")


def show_info(work_dir, name):
    path = get_path(work_dir, name)

    if Folder.exists(path):
        Terminal.write(
            f"Name: {Path.name(path)}\n"
            f"Type: Folder\n"
            f"Empty: {Folder.is_empty(path)}"
        )

    elif File.exists(path):
        Terminal.write(
            f"Name: {Path.name(path)}\n"
            f"Type: File\n"
            f"Extension: {File.extension(path)}\n"
            f"Size: {File.size(path)} bytes"
        )

    else:
        Terminal.error("File or folder not found.")


def main(dictionary):
    work_dir = dictionary["work_dir"]

    Terminal.write("aysExplorer\nType 'help' for available commands.\n")

    while True:
        parts = Terminal.ask(f"{work_dir}> ").strip().split(maxsplit=1)

        if not parts:
            continue

        action = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else ""

        if action == "exit":
            break

        elif action == "cls":
            Terminal.clear()
        
        elif action == "help":
            usage()

        elif action == "pwd":
            Terminal.write(work_dir)

        elif action == "ls":
            list_directory(work_dir)

        elif action == "up":
            if work_dir != "\\":
                work_dir = Path.parent(work_dir)

        elif action == "cd":
            path = get_path(work_dir, argument)

            if argument and Folder.exists(path):
                work_dir = path
            else:
                Terminal.error("Directory not found." if argument else "Usage: cd <directory>")

        elif action == "info":
            if argument:
                show_info(work_dir, argument)
            else:
                Terminal.error("Usage: info <name>")

        else:
            Terminal.error(f"Unknown command: {action}")


if __name__ == "__main__":
    import json

    Terminal.write("DEVELOPER MODE ACTIVE\nexplorer")
    usage()
    main(json.loads(Terminal.ask("enter a dictionary: ")))