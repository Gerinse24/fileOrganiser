#! python3

from tkinter import *
from tkinter import filedialog
import shutil

root = Tk()
root.title("File Organiser")
# Encountered the scope issue with grid_forget() and destroy(). My understanding is that the labels need to be created,
# outside of the created functions to be forgotten and then recreated each time the chosen button is pressed.
my_label = Label(root)
my_label2 = Label(root)
my_label3 = Label(root)


# folderName and folderDest are global variables so shutil can move the file or folder to the chosen destination when,
# the chosen button is pressed.
# Choose the File you wish to move
def fileopen():
    global folderName
    global my_label
    my_label.grid_forget()
    root.folder_name = filedialog.askopenfilename()
    folderName = root.folder_name
    my_label = Label(root, text=root.folder_name)
    my_label.grid(row=0, column=1)


# Choose the Folder to move it too
def filedest():
    global folderDest
    global my_label2
    my_label2.grid_forget()

    root.folder_dest = filedialog.askdirectory()
    folderDest = root.folder_dest
    my_label2 = Label(root, text=root.folder_dest)
    my_label2.grid(row=1, column=1)


# Performs the task of moving the file
def filetomove():
    global my_label3
    my_label3.grid_forget()
    try:
        shutil.move(folderName, folderDest)
        my_label3 = Label(root, text="Complete.")
        my_label3.grid(row=2, column=1)
    except shutil.Error:
        my_label3 = Label(root, text="That File already exists in this Folder.")
        my_label3.grid(row=2, column=1)


my_button = Button(root, text="Open File to Move", command=fileopen, padx=10, pady=10)
my_button.grid(row=0, column=0)

my_button2 = Button(root, text="Destination Folder", command=filedest, padx=10, pady=10)
my_button2.grid(row=1, column=0)

my_button3 = Button(root, text="Move File", command=filetomove, padx=10, pady=10)
my_button3.grid(row=2, column=0)
root.mainloop()

