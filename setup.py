from setuptools import setup

from src import metadata

setup(
    name=metadata.__name__,
    version=metadata.__version__,
    packages=["src", "cli"],
    install_requires=[
        "click",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "swall = cli.cli:swall"
        ],
    },
)
