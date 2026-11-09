from . import Path
import webview
def open(name, path):

    path = Path.convert(path)
    webview.open(name, path)
    webview.start()

if __name__ == "__main__":
    print("this is the aysAPI.")
    print("it is not meant to be run directly.")