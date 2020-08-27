#! python3

from tkinter import *
from tkinter import filedialog
import shutil

explanation = """This is File Organiser.
This program allows you to move a file or files from one location to another.
If a file already exists in a location you can rename the file and save it.
Usage: Click Open Files and choose the files you want to move.
Click Destination and choose a folder to move or save the files to and click Move."""

exsplit = explanation.split('\n')

# Create main window
root = Tk()
root.title("File Organiser - By Geronimo Shaw")

# This frame sits above the listbox at the top of the window.
frame = Frame(root, height=10, width=10)
frame.pack()
label1 = Label(frame, text="File Organiser")
label1.pack()

# This frame contains a listbox which will be used to print text to the screen as tasks
# are performed.
frame2 = Frame(root)
frame2.pack(fill=BOTH, expand=1)
listbox = Listbox(frame2)
listbox.pack(fill=BOTH, expand=1)

for i in range(len(exsplit)):
    listbox.insert(END, exsplit[i])

# This frame contains the buttons and are anchored to the left part of the frame
# so they don't move when the window is resized
frame3 = LabelFrame(root)
frame3.pack(anchor=W)


# This function is called when the "Open" button is clicked. It will open the file dialogue window
# The File that is selected is then inserted into a listbox and the file path is displayed on screen
def fileopen():
    global file_name
    file_name = filedialog.askopenfilename()
    listbox.insert(END, file_name)


def multi_files():
    global filenames
    filenames = filedialog.askopenfilenames(title="Select Files",
                                            filetypes=[("PDF files", "*.pdf"),
                                                       ("ZIP files", "*.zip"),
                                                       ("All files", ".*")], multiple=True)
    for i in range(len(filenames)):
        listbox.insert(END, "File Chosen: " + filenames[i])


# This function is called when the "Destination" button is clicked.
# A file explorer window will show up, only this time asking for a folder location instead of a file.
# The Folder that's selected will again insert on screen for the user
def folderlocation():
    global folder_dest
    folder_dest = filedialog.askdirectory()
    listbox.insert(END, "Move to: " + folder_dest)


# move() is called when the "Move" button is clicked. The function will try to move the file to the chosen location
# except if shutil encounters an error. The user can go back to the destination button and chose a different location.
def move():
    try:
        for i in range(len(filenames)):
            shutil.move(filenames[i], folder_dest)
            listbox.insert(END, "File has been moved.")
    except shutil.Error:
        listbox.insert(END, "The file already exists in this location. Change the name to save it.")
        save_file()


def save_file():
    global file_save
    file_save = filedialog.asksaveasfilename(initialdir=folder_dest, title="Save file",
                                             filetypes=(("ZIP files", "*.zip"), ("All files", "*.*")))
    for i in range(len(filenames)):
        shutil.copyfile(filenames, file_save)
        listbox.insert(END, "The file is renamed and saved")


openbutton = Button(frame3, text="Open Files...", command=multi_files)
openbutton.pack(side=LEFT)

locationbutton = Button(frame3, text="Destination...", command=folderlocation)
locationbutton.pack(side=LEFT)

movebutton = Button(frame3, text="Move...", command=move)
movebutton.pack(side=LEFT)

mainloop()
