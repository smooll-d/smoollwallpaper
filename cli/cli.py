import click

from ..src.SwallVideo import SwallVideo
from ..src.SwallImage import SwallImage

sv = SwallVideo()
si = SwallImage()

@click.command()
def swall_vid():
    sv.swall_video()

@click.command()
def swall_img():
    si.swall_image()
