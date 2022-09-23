#!/usr/bin/python3

import sys

from colorama import init, deinit, Fore, Style

import utils
from config_file import config_file
from start_img_wallpaper import start_img_wallpaper
from SwallLogger import SwallLogger

sl = SwallLogger("swall")

def main():
    init()

    config_file()
    try:
        sl.info("Path = " + config_file.path_img + "\n")
    except AttributeError:
        sl.warning("Please set your path in the swall.conf config file.")
        sl.warning(f"You can find it at \"{utils.CONFIG_FILE}\".")
        sys.exit(0)

    start_img_wallpaper()

    sl.info(Fore.GREEN + "Set wallpaper!" + Style.RESET_ALL)

    deinit()

if __name__ == "__main__":
    main()
