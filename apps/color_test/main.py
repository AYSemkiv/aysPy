import sys
sys.path.append("../..")
from api import Terminal as t

def main():
    t.color(R="50")
    print("Hello, World!")

if __name__ == "__main__":
    
    print("DEVELOPER MODE ACTIVE")
    print("color_test")
    main()
    t.clear_color()