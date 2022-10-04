import sys

from colorama import init, deinit, Fore, Style

from . import utils
from .config_file import SwallConfig
from .start_img_wallpaper import start_img_wallpaper
from .SwallLogger import SwallLogger

sl = SwallLogger("swall")
sc = SwallConfig()

class SwallImage:
    def __init__(self):
        pass

    def swall_image(self):
        init()
    
        sc.read()
        try:
            sl.info("Path = " + sc.config_file.path_img + "\n")
        except AttributeError:
            sl.warning("Please set your path in the swall.conf config file.")
            sl.warning(f"You can find it at \"{utils.CONFIG_FILE}\".")
            sys.exit(0)

        start_img_wallpaper()

        sl.info(Fore.GREEN + "Set wallpaper!" + Style.RESET_ALL)

        deinit()