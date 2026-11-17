import os, importlib, sys, subprocess
from api import Terminal as t, Path as p, Folder as fol, File as fi

t.clear()
sep = os.sep

work_fol = sep
file_fol = p.file_fol

commands = {
  "help": "the command you're in",
  "cf": "change the folder you're in",
  "cf ..": "go a folder up",
  "ls": "list the folder contents",
  "reload": "reload aysPy",
  "exit": "exit aysPy",
  "cts": "clear the screen",
  "app_name.app": "open an app"
}
help_list = t.make_help(commands, "commands:")

default_data = {
  "args": True,
  "file_fol": False,
  "work_fol": False
}

print("""aysPy
type 'help' for available commands.""")

def merge(default_data, metadata):
    merged = default_data.copy()
    merged.update(metadata)
    return merged    

def assemble_data(metadata, tmp_list):

  global file_fol
  global work_fol

  data = {}
  default_data = {
    "args": tmp_list,
    "file_fol": file_fol,
    "work_fol": work_fol
  }

  for key in default_data:
    if key in metadata and metadata[key] == True:
      data[key] = default_data[key]
  return data

def parse_data(metadata):
    result = {}

    if not metadata:
      t.warning("the metadata file of this app is likely empty")
      return

    for item in metadata.split(","):
        key, value = item.split(":")
        result[key] = value == "1"

    return result

def main():
  global work_fol

  comd = t.ask(f"{work_fol}>")

  com_list = t.split(comd)
  
  if com_list == []:
    com_list = [""]
  name = com_list[0]
  print("")

  if name == "exit":
    t.clear()
    sys.exit()

  elif name == "reload":
    subprocess.Popen([sys.executable, p.convert("ays.py")]).wait()
    sys.exit()

  elif name == "help":
    print(help_list)
  
  elif name == "cf":
    if len(com_list) == 1:
      print("usage: 'cf ..' OR 'cf folder'")
    elif com_list[1] == "..":
      work_fol = p.up(work_fol)
    else:
      new_dir = p.join(work_fol, com_list[1])
      if fol.exists(new_dir):
        work_fol = new_dir

  elif name == "ls":
    tmp = fol.list(work_fol)
    print("[FOL] means folder, [FIL] means file \n")
    for i, item in enumerate(tmp):
      temp = p.join(work_fol, item)
      if fi.exists(temp):
        tmp[i] = f"[FIL] {item}"
      elif fol.exists(temp):
        tmp[i] = f"[FOL] {item}"
      else:
        tmp[i] = f"[???] {item}"

    print("\n".join(tmp))

  elif name == "cts":
    t.clear()

  elif name == "":
    pass

  elif name.endswith(".app") and name != ".app":
    comd1 = name.rfind(".app")
    comd2 = name[:comd1]

    app_dir = p.join(f"apps", comd2)

    if fol.exists(app_dir):
      app = importlib.import_module(f"apps.{comd2}.main")

      metadata = {}
      metadata_file = p.join(app_dir, "metadata")

      if fi.exists(metadata_file):
          tmp = fi.read(metadata_file)
          metadata = parse_data(tmp)

      tmp_list = com_list[1:]
      merged_data = merge(default_data, metadata)
      assembled_data = assemble_data(merged_data, tmp_list)

      def this_bs_long(merged_data):
        return any(value is True for value in merged_data.values())

      if merged_data["args"] and len(tmp_list) == 0:
        app.usage()
      elif this_bs_long(merged_data):
        app.main(assembled_data)
      else:
        app.main()

    else:
      print(f"error: '{comd2}' is not a valid app.")

  else:
    if not com_list == [None]:
      print("unknown command.")

if __name__ == "__main__":
  while True:
    main()