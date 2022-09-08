import threading
import sys

from colorama import init, deinit, Fore, Style

import utils
from config_file import config_file
from pause_wallpaper_on_focus_lost import pause_wallpaper_on_focus_lost
from start_wallpaper import start_wallpaper

def main():
    init()

    config_file()
    try:
        print("\nswall: Path = " + config_file.path)
        print("swall: Opacity = " + config_file.opacity)
        print("swall: Priority level = " + config_file.priority)
        print("swall: Pause = " + config_file.pause)
        print("\nswall: Desktop WID = " + config_file.dwid)
    except AttributeError:
        print("\nPlease set your path in the swall.conf config file.")
        print(f"You can find it at \"{utils.CONFIG_FILE}\".")
        sys.exit(0)

    print("\nswall: Creating threads...")
    thread_1 = threading.Thread(target=start_wallpaper)
    thread_2 = threading.Thread(target=pause_wallpaper_on_focus_lost)

    print("swall: Starting threads...")
    if config_file.pause == "true":
        thread_1.start()
        thread_2.start()
    elif config_file.pause == "false":
        thread_1.start()

    print(Fore.GREEN + "\nswall: Running!")
    print(Style.RESET_ALL)

    deinit()

if __name__ == "__main__":
    main()
