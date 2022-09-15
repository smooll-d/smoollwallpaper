import os

import utils
from config_file import config_file

def start_img_wallpaper():
    if utils.XDG_CURRENT_DESKTOP == "GNOME":
        if config_file.colorscheme == "light":
            os.system(f"gsettings set org.gnome.desktop.background picture-uri \"file://{config_file.path_img}\"")
        elif config_file.colorscheme == "dark":
            os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark \"file://{config_file.path_img}\"")
