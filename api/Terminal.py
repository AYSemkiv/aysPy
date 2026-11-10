import os

def clear():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def write(text):

    print(text)

def ask(text):

    return input(f"{text} ").lower().strip()

def confirm(text):

    text = input(f"Y/N: {text} ")
    if text.lower() == "y":
        return True
    elif text.lower() == "n":
        return False
    else:
        return None

def error(text):

    print(f"error: {text}")