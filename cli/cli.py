import click

from src.SwallVideo import SwallVideo
from src.SwallImage import SwallImage
from src.__version__ import __version__

sv = SwallVideo()
si = SwallImage()

def version():
        print(f"SmoollWallpaper v.{__version__} made by Jakub Skowron <jakubskowron676@gmail.com>")

@click.command()
@click.option("--version", is_flag=True, callback=version, is_eager=True, expose_value=False, help="Show version.")
def swall_vid():
    sv.swall_video()

@click.command()
@click.option("--version", is_flag=True, callback=version, is_eager=True, expose_value=False, help="Show version.")
def swall_img():
    si.swall_image()
