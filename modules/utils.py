import os
import sys







# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



global __PROGRESS__
__PROGRESS_CALLBACKS__ = []

def getProgress():
    global __PROGRESS__
    return __PROGRESS__

def increaseProgress():
    global __PROGRESS__
    __PROGRESS__ += 1
    callProgressCallbacks()

def resetProgress():
    global __PROGRESS__
    __PROGRESS__ = 0

def addProgressCallback(f):
    __PROGRESS_CALLBACKS__.append(f)

def callProgressCallbacks():
    global __PROGRESS__
    for f in __PROGRESS_CALLBACKS__:
        f(__PROGRESS__)

