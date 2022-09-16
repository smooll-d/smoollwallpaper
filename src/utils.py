import os

HOME                = os.getenv("HOME")
XDG_CURRENT_DESKTOP = os.getenv("XDG_CURRENT_DESKTOP")
KDE_FULL_SESSION    = os.getenv("KDE_FULL_SESSION") # Only if user's inside KDE

CONFIG_FOLDER = f"{HOME}/.config/swall/"
CONFIG_FILE   = f"{HOME}/.config/swall/swall.conf"
