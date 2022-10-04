import click

from src.SwallVideo import SwallVideo
from src.SwallImage import SwallImage
from src import metadata
from src.config_file import SwallConfig

sv = SwallVideo()
si = SwallImage()
sc = SwallConfig()

def swall_version():
    click.echo(f"{metadata.__name__} v.{metadata.__version__}")

@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, required=False, help="Show version.")
def swall(version):
    """Simple Python script for setting video wallpapers on Linux.
    """
    if version:
        swall_version()
        exit(0)

@swall.command()
@click.option("-p", "--path", required=False, show_default=True, default=sc.path_vid, help="Set path to wallpaper.")
def vid(path):
    """Set video (.mp4) as wallpaper.
    """
    sv.swall_video(path)

@swall.command()
def img():
    """Set image of choice as wallpaper.
    """
    si.swall_image()