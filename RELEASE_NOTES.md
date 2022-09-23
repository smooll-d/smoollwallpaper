# Release notes

Release notes for SmoollWallpaper.

***

## v1.3.0 - SwallLogger | 23/09/2022

### Changed

- Complete overhaul of the logging system (now uses the `logging` library in a file called `SwallLogger.py`. yes I know, I'm good at coming up with cool names)
- Normal KDE wallpapers are currently unavailable, but (hopefully) in the future they will be brought back

### Added

- Added new option - `PATHS` to the config file, so when you download this version please generate a new config file (delete the old config file and run the program)
- GitHub project specific: Added a `test` folder for various tests. There's already a test file in there!

### Fixed

- Fixed the `path` variable in `start_wallpaper.py` so the video wallpaper works now. Sorry :)

## v1.2.2 - LX(DE/Qt) Wallpapers | 18/09/2022

- Added LXDE/PCmanFM and LXQt/PCmanFM-qt wallpaper changing
- For GitHub project: Added `Dependabot`
- For GitHub project: Added `Getting Started (Normal Wallpapers)` wiki page
- And more small changes

## v1.2.1 | 16/09/2022

- Added KDE wallpaper changing
- Removed `colorscheme` option from `swall.conf` config file
- And more small changes

## v1.2.0 | 15/09/2022

- Added picture wallpapers (only on GNOME at the moment)

## v1.1.0 | 06/09/2022

- Added option to not pause the wallpaper when the desktop is not focused

## v1.0.0 | 01/09/2022

- Initial release
