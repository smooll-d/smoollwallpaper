import os
import configparser
import utils

from get_window_id import get_window_id

def config_file():
    get_window_id()

    config = configparser.ConfigParser(allow_no_value=True)
    config.optionxform = str
    config["OPTIONS"] = { "# Path to your wallpaper (video)": None,
                          "path-vid": f"{utils.HOME}/path/to/wallpaper",
                          "\n# Path to your wallpaper (image)": None,
                          "path-img": f"{utils.HOME}/path/to/wallpaper",
                          "\n\n# Opacity level (how transparent should mpv be, from 0 to 1": None,
                          "opacity": 1.0,
                          "\n# Priority level (-20 = highest, 20 = lowest)": None,
                          "priority": 20,
                          "\n# Whether to pause the wallpaper or not when not focused on the desktop": None,
                          "pause": "true" }
    config["VARIABLES"] = { "# Desktop Window ID (DON'T TOUCH!)": None,
                            "dwid": get_window_id.dwid }

    print("swall: Searching for swall.conf...")
    if os.path.exists(utils.CONFIG_FOLDER):
        if os.path.exists(utils.CONFIG_FILE):
            print("swall: swall.conf found!")
            print("swall: Reading swall.conf...")

            config.read(utils.CONFIG_FILE)

            config_file.path_vid = config.get("OPTIONS", "path-vid")
            config_file.path_img = config.get("OPTIONS", "path-img")

            config_file.opacity  = config.get("OPTIONS", "opacity")
            config_file.priority = config.get("OPTIONS", "priority")
            config_file.pause    = config.get("OPTIONS", "pause")

            config_file.dwid     = config.get("VARIABLES", "dwid")

            if config_file.dwid != get_window_id.dwid:
                config_file.dwid = get_window_id.dwid

                config.set("VARIABLES", "dwid", get_window_id.dwid)

                with open(utils.CONFIG_FILE, "w") as configfile:
                    config.write(configfile)
        else:
            print("swall: swall.conf not found!")
            print("swall: Creating swall.conf...")

            with open(utils.CONFIG_FILE, "w") as configfile:
                config.write(configfile)
    else:
        os.makedirs(utils.CONFIG_FOLDER)

        if os.path.exists(utils.CONFIG_FILE):
            print("swall: swall.conf found!")
            print("swall: Reading swall.conf...")

            config.read(utils.CONFIG_FILE)

            config_file.path_vid = config.get("OPTIONS", "path-vid")
            config_file.path_img = config.get("OPTIONS", "path-img")

            config_file.opacity  = config.get("OPTIONS", "opacity")
            config_file.priority = config.get("OPTIONS", "priority")
            config_file.pause    = config.get("OPTIONS", "pause")

            config_file.dwid     = config.get("VARIABLES", "dwid")

            if config_file.dwid != get_window_id.dwid:
                config_file.dwid = get_window_id.dwid

                config.set("VARIABLES", "dwid", get_window_id.dwid)

                with open(utils.CONFIG_FILE, "w") as configfile:
                    config.write(configfile)
        else:
            print("swall: swall.conf not found!")
            print("swall: Creating swall.conf...")

            with open(utils.CONFIG_FILE, "w") as configfile:
                config.write(configfile)
