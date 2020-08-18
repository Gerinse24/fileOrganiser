#! python3
# by Geronimo Shaw

from pathlib import Path
import os
import shutil
import sys

"""This script cleans up your Downloads folder. It will search for certain file extensions and moves those files to the
assigned folder. If the file is a .pdf document, it will be moved to a new folder - PDF - in the Documents folder.
The same thing applies to .zip files."""


"""Prints the users profile to screen that way you know where the script is poking around.
usrFolder and docFolder are WindowsPath values that are converted to strings for navigation.
zipFolder and pdfFolder are WindowsPath values that are used for after the folders are made."""

print("Your home folder is %s " % str(Path.home()))
usrFolder = str(Path.home() / "Downloads")
docFolder = str(Path.home() / "Documents")
pdfFolder = Path.home() / "Documents" / "PDF"
zipFolder = Path.home() / "Documents" / "ZIP"
p = Path(usrFolder)

"""These try/except clauses are to make the folder if it does not exist, except if the folder does exist the program
will move on."""

try:
    os.mkdir(str(pdfFolder))
except FileExistsError:
    print("The PDF folder already exists in Documents.")

try:
    os.mkdir(str(zipFolder))
except FileExistsError:
    print("The ZIP folder already exists in Documents.")

"""Loops through the Downloads folder and checks for different file type extensions. If a match is found shutil will
move that file to the assigned folders. .pdf to Documents/PDF or .zip to Documents/ZIP.
As of right now, those two extensions are the only ones that make separate folders in Documents."""

for fileExt in p.glob("*.pdf"): # Loops through Downloads folder for files with .pdf extension and moves them to PDF.
    try:
        shutil.move(str(fileExt), str(pdfFolder))
    except shutil.Error:
        print("That file already exists in Documents.")

for fileExt in p.glob("*.zip"):
    try:
        shutil.move(str(fileExt), str(zipFolder))
    except shutil.Error:
        print("That file already exists in Documents.")

for fileExt in p.glob("*.docx"):
    try:
        shutil.move(str(fileExt), docFolder)
    except shutil.Error:
        print("That file already exists in Documents.")

for fileExt in p.glob("*.odt"):
    try:
        shutil.move(str(fileExt), docFolder)
    except shutil.Error:
        print("That file already exists in Documents.")

input("Tasks complete. Please press Enter to exit.\n")
sys.exit()
