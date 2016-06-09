from tkinter import *
import tkinter.messagebox
from os.path import expanduser
home_dir = expanduser('~')
pathToSaveVideos = home_dir + "\\Videos"


class MyFirstGUI:
    def __init__(self, master, defaultPath):
        self.master = master
        master.title("Youtube Playlist Downloader")

        frame = Frame(root, width=100, heigh=200, bd=11)
        frame.pack()

        self.label = Label(
            frame, text="Introdueix url de la llista de reproducció",
            width=90)
        self.label.pack()

        df = StringVar()
        df.set(
            """https://www.youtube.com/playlist?list=PLV8ixeX3qFzIkjXW_GpiV1hi_
0ISnG8fA""")
        self.url = Entry(
            frame, validate="key", width=90, textvariable=df)
        # , validatecommand=(vcmd, '%P'))
        self.url.pack()
        self.url.focus()

        self.label2 = Label(
            frame, text="Introdueix carpeta arrel de descarrega",
            width=90)
        self.label2.pack()

        dp = StringVar()
        dp.set(defaultPath)
        self.filepath = Entry(
            frame, validate="key", width=90, textvariable=dp)
        # , validatecommand=(vcmd, '%P'))
        self.filepath.pack()

        self.close_button = Button(
            frame, text="Descargar", command=master.quit)
        self.close_button.pack()

    def validate(self, new_text):
        if not new_text:
            print("field empty")
        # pass

    def get_url(self):
        return self.url.get()

    def get_path(self):
        return self.filepath.get()

root = Tk()
my_gui = MyFirstGUI(root, pathToSaveVideos)
root.mainloop()

pathToSaveVideos = my_gui.get_path()
urlPlayList = my_gui.get_url()

if not pathToSaveVideos or not urlPlayList:
    tkinter.messagebox.showinfo("ERROR", "Some field is empty")
    raise Exception("Some field is empty")
