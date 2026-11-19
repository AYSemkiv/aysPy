# THE BASICS
This is the apps folder, which contains the apps.
There is not just aysAPI; there is metadata too, where you can get basic info  
about aysPy. 

# METADATA 
Here's what metadata can give you:  
1. **args**:  
Get the arguments that the user entered.  
For example, if the user entered:  
example.app "Hello world ii!" ex  
It responds with:
["Hello world ii!", "ex"]
2. **work_fol**:
The working folder of aysPy. 
For example, if aysPy says:  
`\>`  
in the CLI, the working folder is:  
`\`
3. **file_fol**:  
Get the file folder. If `ays.py` is in:  
`C:\Users\Nova\Desktop\os`  
It gives you:  
`C:\Users\Nova\Desktop\os`  

That's it! Currently, no other metadata abilities have been implemented;  
from personal app making, I didn't need any others.  
Oh, and, this is just one part, I haven't even told you how to use it or how to ask aysPy for them.  
By default, `args` is `True`, and `file_fol` & `work_fol` are off.  
To use them, simply use:
main(dictionary)  
And, dictionary["args"] or dictionary["file_fol"], etc.  

# FOLDER STRUCTURE

The basic structure for an aysPy app is:  
``` txt
app/
    metadata (optional)
    main.py
```

## METADATA (CONTINUED)

And, for metadata, if you use it,  
it's like JSON. 1 means `True` and everything else, including 0, means `False`.  
For example:  
`work_fol:1,args:0`.  
It can be in any order, and use commas to separate them.  

# MAIN.PY

There are 2 possible ways main.py can be done:  
1. **If you set all metadata to 0**:
``` python
def main():
    # code goes here
if __name__ == "__main__":
    print("DEVELOPER MODE ACTIVE")
    print("app_name")
    main()
```
2. **If args is on**:
``` python
def main(dictionary):
    # code goes here
def usage():
    print("usage: app_name.app [whatever_here]")
if __name__ == "__main__":
    import json
    print("DEVELOPER MODE ACTIVE")
    print("app_name")
    usage()
    dictionary = json.loads(input("enter a dictionary: "))
    main(dictionary)
```
# FINAL "VERDICT"
aysPy automatically handles usage, aysAPI, and getting the metadata to you.  
You, as a developer, can **actually** focus on getting the code right, instead of  
messing with complicated libraries.  
Developer mode is there so you can run your app directly, instead of going through the mess of  
using aysPy.