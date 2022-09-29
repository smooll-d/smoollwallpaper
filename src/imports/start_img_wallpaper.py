import os

from . import utils
from .config_file import config_file

def start_img_wallpaper():
    # GNOME
    if utils.XDG_CURRENT_DESKTOP == "GNOME":
        os.system(f"gsettings set org.gnome.desktop.background picture-uri \"file://{config_file.path_img}\"")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark \"file://{config_file.path_img}\"")
    # LXDE/PCmanFM
    elif utils.XDG_CURRENT_DESKTOP == "LXDE":
        os.system(f"pcmanfm --set-wallpaper \"{config_file.path_img}\"")
    # LXQt/PCmanFM-qt
    elif utils.XDG_CURRENT_DESKTOP == "LXQt":
        os.system(f"pcmanfm-qt --set-wallpaper \"{config_file.path_img}\"")
