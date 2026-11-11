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

    text = ask(f"Y/N: {text}")
    if text == "y":
        return True
    elif text == "n":
        return False
    else:
        return None

def error(text):

    print(f"error: {text}")

def split(text):
    args = []
    current = ""
    quoted = False

    for char in text:
        if char == '"':
            quoted = not quoted
        elif char == " " and not quoted:
            if current:
                args.append(current)
                current = ""
            else:
                current += char

    if quoted:
        error("unclosed quotation marks")
        return None

    if current:
        args.append(current)

    return args