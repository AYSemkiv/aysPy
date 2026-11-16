import sys
sys.path.append("../..")
from api import Terminal as t, Path as p

def main():
    sep = p.sep
    while True:
        loop()

def loop():
    comd = t.ask("appsman>")

if __name__ == "__main__":
    
    print("DEVELOPER MODE ACTIVE")
    print("appsman")
    main()