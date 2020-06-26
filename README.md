# Media_Player

This is a simple media player written in python. The given files, 100- 1000- 100000- sorted_tracks.txt, contain title and artist of songs downloaded online. Those information are listed line by line under the file. The tksongsearch.py is designed to open those files and tokenized every single line.

## 1. implementation

In this project, the AVL-tree is used to store and arrange title and artist of songs. In order to build AVL-tree, the binary search tree is used as base tree. 
The given AVLtree class is designed,
```python
class AVLTree(BSTree):

    def insert(self, v):
        '''(AVLTree, object) -> NoneType
        Insert a new AVLNode with value v into self.
        Rebalance tree if required.'''

        BSTree.insert(self, AVLNode(v))
        return help_insert(AVLNode(v))

    def delete(self, v):
        '''(AVLTree, object) -> NoneType
        Do nothing and return nothing. Supersede BSTree.delete.
        NOTE: This method is complete.'''

        return None
```
The AVLNode class is implemented,
```python
class AVLNode(BTNode):

    def __repr__(self):
        '''(AVLNode) -> str
        Return the internal string representation of self.
        This method is called when a list of AVLNodes is
        printed.
        NOTE: This method is complete.'''

        return "AVLNode: {}".format(self.value)

    def balance_factor(self):
        '''(AVLNode) -> int
        Return the the height of self's left subtree minus the
        height of self's right subtree.'''

        if self.left == None and self.right == None:
        # as ABLNode has no left and right child.
            return 0
        elif self.left == None:
        # as ABLNode has no left child, but right child
            return - self.right.height
        elif self.right == None:
        # as ABLNode has no right child, but left child
            return self.left.height
        return self.left.height - self.right.height
```

The main file, song.py is composed by title, artist and duration to distingush each songs. The 

```python
class Song:
    '''A Song class.'''

    def __init__(self, single_string):
        '''(Song, string) -> None
        A new Song with title, artist, duration from single_string
        '''

        string_list = single_string.strip().split("<SEP>")
        self.title = string_list[1]
        self.artist = string_list[0]
        self.duration = string_list[2]

    def __str__(self):
        '''(Song) -> str
        Return string in the form "artist - title (duration)"
        '''

        return "{} - {} ({})".format(self.artist, self.title, self.duration)

    def __eq__(self, other):
        '''(Song, object) -> bool
        Return True Iff the song's title, artist and duration are all equal.
        '''

        return (self.title == other.title) and (self.artist == other.artist)\
               and (self.duration == other.duration)

    def __ne__(self, other):
        '''(song, object) -> bool
        Return True iff the song's title, artist and duration are not all equal
        '''

        return not self.__eq__(other)
```

## 2. Stylecheck and unnittest 

The pep8.py and run_style.py are used to check coding style.

````python
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

````
