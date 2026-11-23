import sys
sys.path.append("../..")
from api import Terminal as t

def main():
    t.color(R="255")
    print("This text is red!")
    t.color(G="255")
    print("This text is green!")
    t.color(B="255")
    print("This text is blue!")
    t.color(R="255",G="255")
    print("This text is yellow!")


if __name__ == "__main__":
    
    print("DEVELOPER MODE ACTIVE")
    print("color_test")
    main()
    t.clear_color()