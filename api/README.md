# THE BASICS
The aysAPI is an API to abstract core functions of aysPy.
It includes 5 sub-APIs:


- File
- Folder
- Path
- Terminal
- Window (ALPHA)

I consider aysPy as a buggy system. It’s definitely not the most bulletproof CLI out there.

Before we get into the sub-APIs, here is the basic setup for how to use aysAPI in your apps:

1. **Figure out which sub-APIs you need**  
To figure out the sub-APIs you need, read below or guess what each sub-API does.
2. **Import the library**  
To import the library, use:
``` python
import sys
sys.path.append("../..")
from api import api_name as short_name, another_api_name as short_name
```
My personal example is:
``` python
import sys
sys.path.append("../..")
from api import Terminal as t, Path as p, Folder as fol, File as fi
```
Yes, aysPy literally uses this.

3. **Use the library functions**  
Each library function has a short overview below.
4. **Start using it!**  
Self-explanatory.


# EXPECTATIONS
Since an API is designed to abstract the code, aysAPI does exactly that!  
The root folder isn’t `C:\`, it’s `\`, if you’re on Windows, and `/`, if you’re on UNIX (macOS, Linux, etc).  
Each API function is flexible. For example, you can assume that the separator is / or \ in your code. 
aysAPI handles this automatically. You do need to keep in mind that, aysAPI uses the separator from the OS you’re running on.   However, if your code depends on a specific separator, you can instead use `api.Path.sep` to find out the separator the OS is using.  
`OS` in this documentation means the OS aysPy is running on.

# FILE

The purpose of the file sub-API is to modify files.  
To use any of these API functions, write `api.File.` at the beginning of the function name.  
If there's no description, that means that the function name itself is descriptive.  
Here are all of the up-to-date operations:

## read(path)
Read a file on a specific path. It outputs the files data.

## protected(path)
Checks whether a specific file is protected. The protected file is `ays.py`

## get_file(types)
Lets you open a dialog box to select a file. *Currently, it outputs a non-abstracted path, so be aware.* There will also be an update which implements a lot more ways to open a file, such as opening several files (this will be included in the update)

## create(path, content)
## delete(path)
## move(path, new_path)
## copy(path, new_path)
## exists(path)
Checks whether that file exists.
## rename(path, new_name)

## size(path)
Get the size of a file **in bytes**

## extension(path)
Get the file extension of a file

# Folder
The purpose of the folder sub-API is to modify folders.  
To use any of these API functions, write `api.Folder.` at the beginning of the function name.  
If there's no description, that means that the function name itself is descriptive.  
Here are all of the up-to-date operations:


## protected(path)
Checks whether a specific folder is protected. The protected folders are `apps/` and `api/`

## get_folder()
Lets you open a dialog box to select a folder. *Currently, it outputs a non-abstracted path, so be aware.*  
No, this won't get updated to have a range of folders, as apparently the library I use doesn't support it.

## create(path)
## delete(path)
## move(path, new_path)
## copy(path, new_path)
## exists(path)
Checks whether that folder exists.
## rename(path, new_name)

## list(path)
Lists the items (files or folders) in a folder

## is_empty(path)

# PATH
The purpose of the path sub-API is to alter paths.  
To use any of these API functions, write `api.Path.` at the beginning of the function name.  
If there's no description, that means that the function name itself is descriptive.  
Here are all of the up-to-date operations:

## normalize(path)
Does basic normalization. If your OS separator is `\`, it converts `/` to `\` in paths. Exact same thing vice-versa.

## up(path)
Go up a folder.

## join(path, name)
Join 2 paths together.

## name(path)
Get the name of folder/file from a path.

## convert(path)
Turn an abstracted path into a real path accepted by the OS.

# Terminal
The purpose of the terminal sub-API is to let you more efficiently use I/O.  
To use any of these API functions, write `api.Terminal.` at the beginning of the function name.  
If there's no description, that means that the function name itself is descriptive.  
Here are all of the up-to-date operations:

## clear()
Clear the I/O
## write(text)
Write some text on the I/O
## ask(text)
Ask something to the user.  
Adds a space after question, strips and lowers the text immediately.
## confirm(text)
Confirm something.  
Here's what it would do:
`Y/N: [your_text] `
If the user says yes, it returns `True`.  
If the user says no, it returns `False`.  
If the user doesn't say it, it returns `None`.

## error(text)
Errors out.  
It would do:
`error: [your_error]`
## split(text)
Insanely useful.  
It splits text you input by spaces, and also supports quotes.  
If it errors, it returns `None`

# Window
The purpose of the window sub-API is to let you create web-apps.  
To use any of these API functions, write `api.Window.` at the beginning of the function name.  
If there's no description, that means that the function name itself is descriptive.  
This API is very early-testers.
Here are all of the up-to-date operations:

## open(name, path)
Open a window from a path. `name` means the title you want for the window.

## list()
List the window objects that are currently open.
## close(id)