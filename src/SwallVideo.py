import threading
import sys

from colorama import init, deinit, Fore, Style

from . import utils
from .config_file import SwallConfig
from .pause_wallpaper_on_focus_lost import pause_wallpaper_on_focus_lost
from .start_wallpaper import start_wallpaper
from .SwallLogger import SwallLogger

sl = SwallLogger("swall")
sc = SwallConfig()

class SwallVideo:
    def __init__(self):
        pass

    def swall_video(self, path=sc.path_vid, opacity=sc.opacity, priority=sc.priority, pause=sc.pause):
        init()

        sc.read()
        try:
            sl.info("Path = " + sc.path_vid)
            sl.info("Opacity = " + sc.opacity)
            sl.info("Priority level = " + sc.priority)
            sl.info("Pause = " + sc.pause + "\n")
            sl.info("Desktop WID = " + sc.dwid + "\n")
        except AttributeError:
            sl.warning("Please set your path in the swall.conf config file.")
            sl.warning(f"You can find it at \"{utils.CONFIG_FILE}\".")
            sys.exit(0)
    
        sl.info("Creating threads...")
        thread_1 = threading.Thread(target=start_wallpaper)
        thread_2 = threading.Thread(target=pause_wallpaper_on_focus_lost)
    
        sl.info("Starting threads...\n")
        if sc.pause == "true":
            thread_1.start()
            thread_2.start()
        elif sc.pause == "false":
            thread_1.start()
    
        sl.info(Fore.GREEN + "Running!" + Style.RESET_ALL + "\n")
    
        deinit()