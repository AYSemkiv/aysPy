import os

def clear():
        os.system("cls")

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

if __name__ == "__main__":
    print("this is the aysAPI.")
    print("it is not meant to be run directly.")