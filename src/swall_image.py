import sys

from colorama import init, deinit, Fore, Style

import utils
from config_file import config_file

def main():
    init()

    config_file()
    try:
        print("\nswall: Path = " + config_file.path_img)
    except AttributeError:
        print("\nPlease set your path in the swall.conf config file.")
        print(f"You can find it at \"{utils.CONFIG_FILE}\".")
        sys.exit(0)

    print(Fore.GREEN + "\nswall: Running!")
    print(Style.RESET_ALL)

    deinit()

if __name__ == "__main__":
    main()
