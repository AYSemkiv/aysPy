if __name__ == "__main__":
    import Path
else:
    from . import Path

import webview

def open(name, path):

    path = Path.convert(path)
    webview.open(name, path)
    webview.start()

def list():

    return webview.windows

def close(id):

    webview.windows[id].destroy()