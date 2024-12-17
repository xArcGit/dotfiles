<!-- Title -->
<h1 align="center"><strong>Dotfiles</strong></h1>
<p align="center">Fully-featured floating/tiling window manager-based dotfiles for GNU/Linux</p>

<!-- Introduction -->

## Introduction

This repository contains dotfiles for configuring various components of a GNU/Linux system, including window managers, terminals, file managers, browsers, editors, and more.

### Included Components:

<img src="images/01.png" width="60%" align="right">

| **Component**         | **Name**                                                    |
| :-------------------- | :---------------------------------------------------------- |
| **Window Manager**    | [bspwm](https://github.com/baskerville/bspwm)               |
| **Terminal Emulator** | [kitty](https://sw.kovidgoyal.net/kitty/)                   |
| **File Manager**      | [yazi](https://github.com/sxyazi/yazi)                      |
| **Text Editor**       | [nvim](https://neovim.io/)                                  |
| **PDF Viewer**        | [zathura](https://pwmt.org/projects/zathura/)               |
| **Video Player**      | [mpv](https://mpv.io)                                       |
| **Music Player**      | [spotify_player](https://github.com/aome510/spotify-player) |
| **Browser**           | [zen-browser](https://github.com/zen-browser/desktop)       |
| **System Monitor**    | [htop](https://htop.dev/)                                   |
| **Display Manager**   | [ly](https://github.com/fairyglade/ly)                      |

## Installation

> **Warning**: This setup script is designed for Arch Linux and its derivatives. Running it on other distributions may cause unexpected behavior or system breakage.

1. Clone this repository:

   ```bash
   git clone git@github.com:xArcGit/dotfiles.git
   ```

   or

   ```bash
   git clone https://github.com/xArcGit/dotfiles.git
   ```

2. Navigate to the dotfiles directory:

   ```bash
   cd dotfiles
   ```

3. Run script:

   ```bash
   chmod +x install
   ./install
   ```

4. Install the required packages

- check [Theme](theme/Readme.md)

## Color Schemes

### [Catppuccin](https://catppuccin.com/)

<p align="center">
  <img src="images/01.png" width="30%">
  <img src="images/02.png" width="30%">
  <img src="images/03.png" width="30%">
</p>
<p align="center">
  <img src="images/04.png" width="30%">
  <img src="images/05.png" width="30%">
  <img src="images/06.png" width="30%">
</p>

For more customization options, please refer to the [options README](options/README.md). This file contains detailed information on how to tweak and personalize various aspects of the dotfiles to better suit your preferences and workflow.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
