import os
import dbus

import utils
from config_file import config_file

def setKDEwallpaper(filepath, plugin="org.kde.image"):
    jscript = """
var allDesktops = desktops();
for (i = 0; i < allDesktops.length; i++) {
    d = allDesktops[i];
    d.wallpaperPlugin = "%s";
    d.currentConfigGroup = Array("Wallpaper", "%s", "General");
    d.writeConfig("Image", "file://%s")
}
"""
    bus = dbus.SessionBus();
    plasma = dbus.Interface(bus.get_object(
        "org.kde.plasmashell", "/PlasmaShell"), dbus_interface="org.kde.PlasmaShell")
    plasma.evaluateScript(jscript % (plugin, plugin, filepath))

def start_img_wallpaper():
    # GNOME
    if utils.XDG_CURRENT_DESKTOP == "GNOME":
        os.system(f"gsettings set org.gnome.desktop.background picture-uri \"file://{config_file.path_img}\"")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark \"file://{config_file.path_img}\"")
    # KDE >= 5.7
    elif utils.KDE_FULL_SESSION == True:
        setKDEwallpaper(config_file.path_img)
    # LXDE/PCmanFM
    elif utils.XDG_CURRENT_DESKTOP == "LXDE":
        os.system(f"pcmanfm --set-wallpaper \"{config_file.path_img}\"")
    # LXQt/PCmanFM-qt
    elif utils.XDG_CURRENT_DESKTOP == "LXQt":
        os.system(f"pcmanfm-qt --set-wallpaper \"{config_file.path_img}\"")
