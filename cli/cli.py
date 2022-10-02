import click

from src.SwallVideo import SwallVideo
from src.SwallImage import SwallImage
from src import metadata

sv = SwallVideo()
si = SwallImage()

def swall_version():
    click.echo(f"{metadata.__name__} v.{metadata.__version__}")

@click.group(invoke_without_command=True)
@click.option("-v", "--version", is_flag=True, required=False, help="Show version.")
def swall(version):
    """_summary_
    """
    if version:
        swall_version()
        exit(0)

@swall.command()
def vid():
    """Set video (.mp4) as wallpaper.
    """
    sv.swall_video()

@swall.command()
def img():
    """Set image of choice as wallpaper.
    """
    si.swall_image()