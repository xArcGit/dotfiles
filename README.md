<!-- Title -->
<h1 align="center"><strong>Dotfiles</strong></h1>

<!-- Images -->
<p align="center">
  <img src="./images/image.png" width="65%">
</p>

<!-- Description -->
<p align="center">Fully-featured floating/tiling window manager-based dotfiles for Arch Linux</p>

<!-- Table of Contents -->

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Color Schemes](#color-schemes)
- [Usage](#usage)
- [Tutorial](#tutorial)
- [Contributing](#contributing)
- [License](#license)

<!-- Introduction -->

## Introduction

This repository contains dotfiles for configuring various components of a Linux system, including window managers, terminals, file managers, browsers, editors, and more.

### Included Components:

| **Component**         | **Name**                                      |
| :-------------------- | :-------------------------------------------- |
| **Window Manager**    | [bspwm](https://github.com/baskerville/bspwm) |
| **Terminal Emulator** | [kitty](https://sw.kovidgoyal.net/kitty/)     |
| **File Manager**      | [ranger](https://ranger.github.io/)           |
| **Browser**           | [brave](https://brave.com/)                   |
| **Text Editor (TUI)** | [astronvim](https://astronvim.com/)           |
| **PDF Viewer**        | [zathura](https://pwmt.org/projects/zathura/) |
| **Video Player**      | [mpv](https://mpv.io)                         |
| **Music Player**      | [ncmpcpp](https://github.com/ncmpcpp/ncmpcpp) |
| **System Monitor**    | [htop](https://htop.dev/)                     |
| **Display Manager**   | [ly](https://github.com/fairyglade/ly)        |

<!-- Installation -->

## Installation

**Note:** You need to be logged in as a regular user to use this script.

1. Install [Git](https://git-scm.com/) if you don't have it:

   ```bash
   sudo pacman -S git
   ```

2. Clone this repository:

   ```bash
   git clone git@github.com:xArcGit/dotfiles.git
   ```

   or

   ```bash
   git clone https://github.com/xArcGit/dotfiles.git
   ```

3. Navigate to the dotfiles directory:

   ```bash
   cd dotfiles
   ```

4. Run the installation script:

   ```bash
   chmod +x install && ./install
   ```

5. Follow the on-screen instructions.

6. Restart your computer.

7. You're done! Now you can enjoy a fully-featured floating/tiling window manager on your computer.

**Note:** Edit `.xinitrc` file and change display settings.

## Color Schemes

These dotfiles include Pywal-based color schemes.

- `Shift` + `Alt` + `w` for changing wallpaper
- wallpaper dir -> `~/Pictures/Wallpapers`
<p align="center">
  <img src="images/img_00.png" width="30%">
  <img src="images/img_01.png" width="30%">
  <img src="images/img_03.png" width="30%">
</p>
<p align="center">
  <img src="images/img_04.png" width="30%">
  <img src="images/img_05.png" width="30%">
  <img src="images/img_06.png" width="30%">
</p>
<p align="center">
  <img src="images/img_07.png" width="30%">
  <img src="images/img_08.png" width="30%">
  <img src="images/img_09.png" width="30%">
</p>

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

