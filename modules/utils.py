
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