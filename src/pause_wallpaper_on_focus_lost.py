import os

from get_window_id import get_window_id
from config_file import config_file

def pause_wallpaper_on_focus_lost():
    try:
        while True:
            get_window_id()
            print("swall: Active WID: " + get_window_id.awid, end="\r")

            if get_window_id.awid != config_file.dwid:
                os.system("kill -STOP $(pgrep mpv)")
            else:
                os.system("kill -CONT $(pgrep mpv)")
    except KeyboardInterrupt:
        os.system("killall \"swall.py\"")
