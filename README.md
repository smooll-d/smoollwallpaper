# SmoollWallpaper

<p align="center">
	<img src="./assets/swlogo.png" />
	<sub><i>"Smooll" pronounced "small".</i></sub>
</p>

SmoollWallpaper (swall, pronounced `swall` and not `s-wall`) is a simple Python script for setting video wallpapers on Linux.

***

<p align="center">
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/releases/tag/v1.3.0" alt="Version">
		<img src="https://img.shields.io/badge/VERSION-1.3.0-pink?style=for-the-badge" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/issues/" alt="Issues">
		<img src="https://img.shields.io/github/issues/reallySmooll/smoollwallpaper?style=for-the-badge&color=brightgreen" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/pulls" alt="Pull Request">
		<img src="https://img.shields.io/github/issues-pr/reallySmooll/smoollwallpaper?style=for-the-badge&color=darkblue" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/stargazers" alt="Stars">
		<img src="https://img.shields.io/github/stars/reallySmooll/smoollwallpaper?style=for-the-badge&color=gold" />
	</a>
</p>

<p align="center">
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/wiki/Getting-Started" alt="Getting Started">
		<img src="https://img.shields.io/badge/GETTING-STARTED-green?style=for-the-badge" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/wiki/Getting-Started-(Normal-Wallpapers)" alt="Getting Started (Normal Wallpapers)">
		<img src="https://img.shields.io/badge/GETTING STARTED-(NORMAL WALLPAPERS)-33ffa5?style=for-the-badge" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/wiki/Getting-Started-(Contributing)" alt="Getting Started (Contributing)">
		<img src="https://img.shields.io/badge/GETTING STARTED-(CONTRIBUTING)-blue?style=for-the-badge" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/blob/master/RELEASE_NOTES.md" alt="Release Notes">
		<img src="https://img.shields.io/badge/RELEASE-NOTES-yellow?style=for-the-badge" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/LICENSE-MIT-orange?style=for-the-badge" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/blob/master/CONTRIBUTING.md" alt="Contributing">
		<img src="https://img.shields.io/badge/CONTRIBUTING-THANKS :)-red?style=for-the-badge" />
	</a>
	<a href="https://www.github.com/reallySmooll/smoollwallpaper/blob/master/CODE_OF_CONDUCT.md" alt="Code of Conduct">
		<img src="https://img.shields.io/badge/CODE OF-CONDUCT-purple?style=for-the-badge" />
	</a>
</p>

***

## Overview
SmoollWallpaper uses the magic of `mpv` and `xwinwrap` to display animated (or just video) wallpapers on your desktop, and with the help of `xprop` it allows the wallpapers to stop when you click on another window than your desktop, if you're PC or laptop don't have the best of specs just like me :).

It also allows using images as wallpapers, but this option is `WIP` (Work In Progress) and only available for `GNOME`, `LXDE/PCmanFM`, `LXQt/PCmanFM-qt` and `KDE >=5.7`, although I don't know about KDE because I haven't tested it yet, but if you'd like to contribute to this project, you can test it out and let me know by opening an issue.

If you'd like to get started on using my magnum opus ('cause let's be honest, I will probably never make something better), you can go to the [Getting Started wiki page](https://www.github.com/reallySmooll/smoollwallpaper/wiki/Getting-Started) or you can click on one of the badges above that says `GETTING STARTED`. There's a normal wallpaper version as well. You can go [here](https://www.github.com/reallySmooll/smoollwallpaper/wiki/Getting-Started-(Normal-Wallpapers)) or you can click on the `GETTING STARTED (NORMAL WALLPAPERS)` badge above.

Happy desktop customization! :D

[![Codacy Security Scan](https://github.com/reallySmooll/smoollwallpaper/actions/workflows/codacy.yml/badge.svg?branch=master)](https://github.com/reallySmooll/smoollwallpaper/actions/workflows/codacy.yml) [![Python application](https://github.com/reallySmooll/smoollwallpaper/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/reallySmooll/smoollwallpaper/actions/workflows/python-app.yml)

***

## Features

- [x] Video wallpapers

- [x] Script pauses automatically if desktop is not focused

- [x] Option to not pause the script automatically when the desktop is not focused

- [x] Normal wallpapers (desktops supported):
	- GNOME

- [ ] Full rewrite with graphical interface (coming, v2.0.0)

I will come up with more features in the future :)

***

### NOTE: THIS SCRIPT ONLY WORKS ON LINUX (X11)
