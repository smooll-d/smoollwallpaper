import os

from .config_file import SwallConfig

sc = SwallConfig()

def start_wallpaper():
    os.system(f"nice -n {sc.priority} xwinwrap -fs -fdt -nf -ni -b -un -o {sc.opacity} -- mpv -wid WID --loop --no-audio --vo=gpu --no-terminal {sc.path_vid}")
