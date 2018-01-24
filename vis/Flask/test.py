import io
import os

from flask import Flask, request

def foo():
    # absolute path of ROOT directory
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'static/data/')
    filename = 'file.txt'

    if not os.path.isdir(target):
        os.mkdir(target)

    file1 = open(target + filename, "w")
    print(target + filename)
    file1.write("Hello!")
    file1.close()
if __name__ == '__main__':
    foo()