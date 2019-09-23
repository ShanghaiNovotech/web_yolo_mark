#!/usr/bin/env python3
import glob
import os
import pathlib

jpg_file_paths = list(pathlib.Path().glob("**/*.jpg"))
jpg_files = sorted(list(map(str, jpg_file_paths)))

for jpg in jpg_files:
    print(jpg)
