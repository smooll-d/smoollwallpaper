#!/usr/bin/python3

import os
import subprocess

print("SmoollWallpaper Dependency Installer (swallDI) v1.0.0")

distro_choice = input("""\nPlease choose your Linux distribution
1. Arch Linux
2. Ubuntu

Choice: """)

if distro_choice == "1":
    """os.system("clear")

    print("Updating system (pacman -Sy)...\n")
    os.system("sudo pacman -Sy")

    print("Installing xwinwrap...")
    os.system("sudo pacman -S --needed xorg-server base-devel libx11 xorgproto libxrender libxext")
    os.system("git clone https://github.com/ujjwal96/xwinwrap.git")
    os.system("cd xwinwrap")
    os.system("make")
    os.system("sudo make install")
    os.system("make clean")
    os.system("cd ..")
    rm_choice = input("\nDone. Would you like to remove the xwinwrap directory? [y/N]: ")

    if rm_choice == "y":
        os.system("rm ./xwinwrap/")
    elif rm_choice == "n" or "":
        print("Not removing.")
    else:
        print("Input not recognized... Not removing.")
"""
    print("Checking if Python >=3.6 is installed...")
    check_version = subprocess.check_output("python --version", shell=True, encoding="utf8")
    version = check_version.strip("Python ")

    if "3.6" in version:
        print("Done.")
    elif "3.7" in version:
        print("Done.")
    elif "3.8" in version:
        print("Done.")
    elif "3.9" in version:
        print("Done.")
    elif "3.10" in version:
        print("Done.")
    else:
        print(f"\nPython version is not 3.6. Python version: {version}")
        should_update = input("Would you like to update? [Y/n]: ")

        if should_update == "y" or "":
            os.system("sudo pacman -Sy python")
        elif should_update == "n":
            print("Not updating.")
        else:
            print("Input not recognized... Not removing.")
