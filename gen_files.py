import glob
import os
import pathlib

jpg_file_paths = list(pathlib.Path().glob("**/*.jpg"))
jpg_files = list(map(str, jpg_file_paths)).sort()

for jpg in jpg_files:
    print(jpg)