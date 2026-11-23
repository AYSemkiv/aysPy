import sys
sys.path.append("..")
from api import Terminal as t

def main(code):

    idx = 0
    while True:
        code_line = code[idx]
        decode = t.split(code_line)
        

    return