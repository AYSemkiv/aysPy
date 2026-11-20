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

def warning(text):

    print(f"warning: {text}")

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
        else:
            current += char

    if quoted:
        error("unclosed quotation marks")
        return None
    if current:
        args.append(current)
    return args

def make_table(definitions, title=None, separator=""):

    if isinstance(definitions, list):
        definitions = dict.fromkeys(definitions, None)

    text = ""
    if not title == None:
        text = f"{title}\n\n"
    keys = list(definitions)
    length = len(keys)

    for i in range(length):
        comd = keys[i]
        defn = definitions[comd]
        if defn == None:
            text = f"{text}{comd}\n"
        elif not defn == None:
            text = f"{text}{comd}{separator} {defn}\n"

    return text

def color(R="0", G="0", B="0"):

    print(f"\033[38;2;{R};{G};{B}m")

def clear_color():

    print("\033[0m")