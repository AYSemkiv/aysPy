import os
import importlib
import sys
import subprocess
from api import Terminal as t, Path as p, Folder as fol, File as fi

t.clear()
sep = os.sep

work_dir = sep
file_dir = os.path.dirname(os.path.abspath(__file__))

default_data = {
  "args": True,
  "file_dir": False,
  "work_dir": False
}

print("""aysPy
type 'help' for available commands.""")

def merge(default_data, metadata):
    merged = default_data.copy()
    merged.update(metadata)
    return merged    

def main():
  global work_dir

  comd = t.ask(f"{work_dir}>")

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
    print("commands: \n"
    "help: the command you're in\n"
    "cf: change the folder you're in\n"
    "cf .. : go a folder up\n"
    "ls: list the folder contents\n"
    "reload: reload aysPy\n"
    "exit: exit aysPy\n"
    "cts: clear the screen\n"
    "app_name.app: open an app\n")

  elif name == "cf":
    if len(com_list) == 1:
      print("usage: 'cf ..' OR 'cf folder'")
    elif com_list[1] == "..":
      work_dir = p.up(work_dir)
    else:
      new_dir = p.join(work_dir, com_list[1])
      if fol.exists(new_dir):
        work_dir = new_dir

  elif name == "ls":
    tmp = fol.list(work_dir)
    print("[FOL] means folder, [FIL] means file \n")
    for i, item in enumerate(tmp):
      temp = p.join(work_dir, item)
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

    app_dir = p.join(f"{sep}apps", comd2)

    if fol.exists(app_dir):
      app = importlib.import_module(f"apps.{comd2}.main")

      metadata = {}
      metadata_file = p.join(app_dir, "metadata")

      if fi.exists(metadata_file):
          tmp = fi.read(metadata_file)
          metadata = t.split(tmp)

      tmp_list = com_list[1:]
      merged_data = merge(default_data, metadata)
      assembled_data = assemble_data(merged_data, tmp_list)

      def this_bs_long(merged_data):
        return any(value is True for value in merged_data.values())
      
      if this_bs_long(merged_data):
        app.main(assembled_data)
      elif merged_data["args"] and len(tmp_list) == 0:
        app.usage()
      else:
        app.main()

    else:
      print(f"error: '{comd2}' is not a valid app.")

  else:
    if not com_list == [None]:
      print("unknown command.")

def assemble_data(metadata, tmp_list):

  global file_dir
  global work_dir

  data = {}
  default_data = {
    "args": tmp_list,
    "file_dir": file_dir,
    "work_dir": work_dir
  }

  for key in default_data:
    if key in metadata and metadata[key] == True:
      data[key] = default_data[key]
  return data

if __name__ == "__main__":
  while True:
    main()