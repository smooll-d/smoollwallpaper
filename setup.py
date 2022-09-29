from setuptools import setup, find_packages

setup(
    name="SmoollWallpaper",
    version="1.4.0-alpha.23",
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
