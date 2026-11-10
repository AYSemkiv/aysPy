from . import Path
import webview

def open(name, path):

    path = Path.convert(path)
    webview.open(name, path)
    webview.start()