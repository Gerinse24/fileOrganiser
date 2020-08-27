# organiser.py

A simple file organiser program. File Organiser is built with Python 3.8, and utilises the tkinter module for GUI creation and File Dialogue. It was packed into an .exe with pyinstaller. The shutil module is used to perform the tasks of moving files or in some cases copying files. Compared to fileOrganiser.py, this is a more free-choice variant and does not limit you to one assigned folder.

As of right now, testing has only been performed on Windows 10. I do not have access to MacOS or Linux based systems for platform testing.

Four functions are used to perform tasks:

# multi_files()

When the function is called - by clicking the Open Files button - a tk.FileDialogue.askopenfilenames object is returned with a list of the selected files. Using a for loop and range to iterate through the returned list, each value is inserted to a ListBox and printed on to the screen. The list is saved in a variable and is assigned to the global scope. This function also handles single files.

# folderlocation()

When the function is called - by clicking the Destination button - a tk.FileDialogue.askdirectory object is returned. The Destination path is stored with a variable and assigned to the global scope.

# move()

When the function is called - by clicking the Move button - a try and except block is entered. Firstly, the try portion contains a for loop which iterates the length of filenames variable created in multi_files() and attempts to move the file at filenames[i] to the selected folder Destination. Except if the file already exists at the location, then the save_file() function is called.

# save_file()

This function is called when a file already exists in folderlocation. A tk.FileDialogue.asksaveasfilename will open the Dialogue window allowing the user to rename the file or even move it to another folder location.

This program will keep running until you close it so lots of files can be moved. BUGS ARE GOING TO BE ENCOUNTERED.
