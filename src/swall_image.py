import sys

from colorama import init, deinit, Fore, Style

import utils
from config_file import config_file
from convert_all_to_bmp import convert_all_to_bmp
from start_img_wallpaper import start_img_wallpaper

def main():
    init()

    config_file()
    convert_all_to_bmp()
    try:
        print("\nswall: Path = " + config_file.path_img)
        print("swall: Converted image path = " + convert_all_to_bmp.converted_image_path)
    except AttributeError:
        print("\nPlease set your path in the swall.conf config file.")
        print(f"You can find it at \"{utils.CONFIG_FILE}\".")
        sys.exit(0)

    start_img_wallpaper()

    print(Fore.GREEN + "\nswall: Set wallpaper!")
    print(Style.RESET_ALL)

    deinit()

if __name__ == "__main__":
    main()
