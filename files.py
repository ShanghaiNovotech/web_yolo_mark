import glob
import os
import pathlib
everything = pathlib.Path().glob("**/*.jpg").sort()

cwd = os.getcwd()
jpg_files = (glob.glob("**/*.jpg")) 
for jpg in everything:
    print(jpg)
