from setuptools import setup, find_packages

from src.__version__ import __version__

setup(
    name="SmoollWallpaper",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "click",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "swall-vid = cli.cli:swall_vid",
            "swall-img = cli.cli:swall_img",
        ],
    },
)
