#!/usr/local/bin/python3.2
import tkinter
from tkinter.filedialog import askopenfilename
import sys

import pep8

if __name__ == "__main__":
    root = tkinter.Tk()
    py_file = askopenfilename(title="Select a Python file to stylecheck ...",
                              initialdir=".")
    if not py_file:
        sys.exit("No file selected")

    pep8.process_options(['-v', '--count', py_file])
    pep8.input_file(py_file)
    if pep8.get_statistics() == []:
        print("Congrats! No style errors were detected.")
