import sys
sys.path.append("..")
from api import Terminal as t

def main(code):

    global idx
    while True:
        code_line = code[idx]
        decode = t.split(code_line)
        if idx == len(code):
            break


        idx += 1

    return