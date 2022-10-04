import os

from . import utils
from .config_file import SwallConfig

sc = SwallConfig()

def start_img_wallpaper():
    # GNOME
    if utils.XDG_CURRENT_DESKTOP == "GNOME":
        os.system(f"gsettings set org.gnome.desktop.background picture-uri \"file://{sc.path_img}\"")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark \"file://{sc.path_img}\"")
    # LXDE/PCmanFM
    elif utils.XDG_CURRENT_DESKTOP == "LXDE":
        os.system(f"pcmanfm --set-wallpaper \"{sc.path_img}\"")
    # LXQt/PCmanFM-qt
    elif utils.XDG_CURRENT_DESKTOP == "LXQt":
        os.system(f"pcmanfm-qt --set-wallpaper \"{sc.path_img}\"")
