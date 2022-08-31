import os

from config_file import config_file

def start_wallpaper():
    os.system(f"nice -n {config_file.priority} xwinwrap -fs -fdt -nf -ni -b -un -o {config_file.opacity} -- mpv -wid WID --loop --no-audio --vo=gpu --no-terminal {config_file.path}")
