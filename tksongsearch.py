from tkinter import *
from tkinter import ttk
from avl import *
from song import *
import sys


class SongSearchApp:

    def __init__(self):
        self.root = Tk()
        self.root.title("Song Search")

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.search = StringVar()
        self.search_entry = ttk.Entry(self.mainframe, width=7, \
                                                    textvariable=self.search)
        self.search_entry.grid(column=0, row=1, sticky=(W, E))

        ttk.Label(self.mainframe, text="Songs").grid(column=0, row=2, \
                                                            sticky=(W, E))
        self.listbox1 = Listbox(self.mainframe, width=50, height=12,\
                                                        selectmode=SINGLE)
        self.listbox1.grid(row=3, column=0)
        self.yscroll = Scrollbar(self.mainframe, command=self.listbox1.yview,\
                                                            orient=VERTICAL)
        self.yscroll.grid(row=3, column=1, sticky=(N, S))
        self.listbox1.configure(yscrollcommand=self.yscroll.set)

        ttk.Label(self.mainframe, text="Artists").grid(column=0, row=4, \
                                                                sticky=(W, E))

        self.listbox2 = Listbox(self.mainframe, width=50, height=12,\
                                                            selectmode=SINGLE)
        self.listbox2.grid(row=5, column=0)
        self.yscroll1 = Scrollbar(self.mainframe, \
                command=self.listbox2.yview, orient=VERTICAL)
        self.yscroll1.grid(row=5, column=1, sticky=(N, S))
        self.listbox2.configure(yscrollcommand=self.yscroll1.set)
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.songpop = songs.starts_with("")
        self.artistpop = artists.starts_with("")
        for item in self.songpop:
            self.listbox1.insert(END, item)
        for item in self.artistpop:
            self.listbox2.insert(END, item)

        self.search_entry.focus()
        self.search.trace("w", self.textChanged)
        self.root.mainloop()

    def textChanged(self, *args):
        self.listbox1.delete(0, END)
        self.listbox2.delete(0, END)
        searchstring = self.search.get()
        if searchstring:
            for item in songs.starts_with(self.search.get()):
                self.listbox1.insert(END, item)
            for item in artists.starts_with(self.search.get()):
                self.listbox2.insert(END, item)
    
    # update Recursion depth limit 
    sys.setrecursionlimit(100000)

if __name__ == '__main__':

    songs = AVLTree()
    artists = AVLTree()

    file = open("10000_sorted_tracks.txt", 'r')
    data = file.readlines()
    l = len(data)
    print("Loading {:d} songs".format(l))
    file.close()
    for line in range(l):
        if not line % (l // 20):
            print("Loading...{}%".format(line // (l // 100)))
        s = Song(data[line])
        song = s.title
        artist = s.artist
        songpair = Pair(song, s)
        songs.insert(songpair)
        artistpair = Pair(artist, s)
        artists.insert(artistpair)
    s = SongSearchApp()
