"""This setup file build executable file game."""
# To build run in terminal  ....\> py setup.py build

# This code is copied from official source of cx-freeze (link:
# 'https://cx-freeze.readthedocs.io/en/latest/distutils.html#distutils-setup-script')

import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = "Win32GUI"
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Save The Ball",
    version="0.1",
    description="The ball needs your help",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
