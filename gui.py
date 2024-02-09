import eel

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

eel.init('static_web_folder')
eel.start('index.html')