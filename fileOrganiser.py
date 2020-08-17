#! python3
# By Geronimo Shaw - 17-08-2020

import os
import sys
import shutil
from pathlib import Path

print("This program checks your Downloads folder for PDF, txt, exe, zip files and moves them to the corresponding \n"
      "folders.\n"
      "PDF/txt/zip files are moved to your Documents folder.\n"
      "A folder called AppInstallers will be made at C:\\Users\\profile\\AppInstallers")
usrFolder = Path.home()     # this should determine the users profile path
dlFolder = Path("Downloads")
# I want to create a windows path value of "Downloads" as every windows profile has this folder
abPath = str(usrFolder / dlFolder)  # add the windows path values together and convert to a string
docFolder = Path("Documents")
docPath = str(usrFolder / docFolder)
appFolder = Path("AppInstallers")
appPath = str(usrFolder / appFolder)
#
#
#

os.chdir(abPath)    # change current working directory to /users/profile/Downloads
p = Path(abPath)
for fileName in p.glob('*.pdf'):    # checks for files with the .pdf extension
    docName = Path(fileName)
    shutil.move(str(docName), docPath)  # moves it to the documents folder


for fileName in p.glob('*.txt'):    # checks for file with .txt extension
    docName = Path(fileName)
    shutil.move(str(docName), docPath)  # moves it to the documents folder


for fileName in p.glob('*.exe'):
    appName = Path(fileName)
    shutil.move(str(appName), appPath)

for fileName in p.glob('*.zip'):
    zipName = Path(fileName)
    shutil.move(str(zipName), docPath)

print("Tasks complete.")
input("Press Enter to exit...")


sys.exit()
