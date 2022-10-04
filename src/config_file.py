import os
import configparser

from . import utils
from .get_window_id import get_window_id
from .SwallLogger import SwallLogger

sl = SwallLogger("config_file")

class SwallConfig:
    def __init__(self, verbose=True):
        self.verbose  = verbose
        self.path_vid = ""
        self.path_img = ""
        self.opacity  = 0
        self.priority = 0
        self.pause    = ""
        self.dwid     = get_window_id.dwid

        get_window_id()
        
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.optionxform = str
        self.config["PATHS"] = { "\n# Path to your wallpaper (video)": None,
                                 "path-vid": f"{utils.HOME}/path/to/wallpaper",
                                 "\n# Path to your wallpaper (image)": None,
                                 "path-img": f"{utils.HOME}/path/to/wallpaper" }
        self.config["OPTIONS"] = { "\n# Opacity level (how transparent should mpv be, from 0 to 1": None,
                                   "opacity": 1.0,
                                   "\n# Priority level (-20 = highest, 20 = lowest)": None,
                                   "priority": 20,
                                   "\n# Whether to pause the wallpaper or not when not focused on the desktop": None,
                                   "pause": "true" }
        self.config["VARIABLES"] = { "\n# Desktop Window ID (DON'T TOUCH!)": None,
                                     "dwid": get_window_id.dwid }
        
    def read(self):
        if self.verbose:
            sl.info("Searching for swall.conf...")
        if os.path.exists(utils.CONFIG_FOLDER):
            if os.path.exists(utils.CONFIG_FILE):
                if self.verbose:
                    sl.info("swall.conf found!")
                    sl.info("swall: Reading swall.conf...\n")

                self.config.read(utils.CONFIG_FILE)

                self.path_vid = self.config.get("PATHS", "path-vid")
                self.path_img = self.config.get("PATHS", "path-img")

                self.opacity  = self.config.get("OPTIONS", "opacity")
                self.priority = self.config.get("OPTIONS", "priority")
                self.pause    = self.config.get("OPTIONS", "pause")

                self.dwid     = self.config.get("VARIABLES", "dwid")

                if self.dwid != get_window_id.dwid:
                    self.dwid = get_window_id.dwid

                    self.config.set("VARIABLES", "dwid", get_window_id.dwid)

                    with open(utils.CONFIG_FILE, "w") as configfile:
                        self.config.write(configfile)
            else:
                if self.verbose:
                    sl.info("swall.conf not found!")
                    sl.info("Creating swall.conf...\n")

                with open(utils.CONFIG_FILE, "w") as configfile:
                    self.config.write(configfile)
        else:
            os.makedirs(utils.CONFIG_FOLDER)

            if os.path.exists(utils.CONFIG_FILE):
                if self.verbose:
                    sl.info("swall.conf found!")
                    sl.info("Reading swall.conf...\n")

                self.config.read(utils.CONFIG_FILE)

                self.path_vid = self.config.get("PATHS", "path-vid")
                self.path_img = self.config.get("PATHS", "path-img")

                self.opacity  = self.config.get("OPTIONS", "opacity")
                self.priority = self.config.get("OPTIONS", "priority")
                self.pause    = self.config.get("OPTIONS", "pause")

                self.dwid     = self.config.get("VARIABLES", "dwid")

                if self.dwid != get_window_id.dwid:
                    self.dwid = get_window_id.dwid

                    self.config.set("VARIABLES", "dwid", get_window_id.dwid)

                    with open(utils.CONFIG_FILE, "w") as configfile:
                        self.config.write(configfile)
            else:
                if self.verbose:
                    sl.info("swall.conf not found!")
                    sl.info("Creating swall.conf...\n")

                with open(utils.CONFIG_FILE, "w") as configfile:
                    self.config.write(configfile)
        
    def write(self, var, config_var):
        if os.path.exists(utils.CONFIG_FILE):
            if self.verbose:
                sl.info(f"Writing variable: {var} to {utils.CONFIG_FILE}...")
            
            self.config.read(utils.CONFIG_FILE)
            
            self.var = self.config.get(config_var, var)
            temp_var = self.var
            self.config.set(config_var, var, temp_var)
            
            with open(utils.CONFIG_FILE, "w") as configfile:
                self.config.write(configfile)