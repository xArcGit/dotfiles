#!/usr/bin/env zsh

# Loading Scripts
PATH="$HOME/.config/bspwm/scripts:$PATH"

# Display Setup
# DISPLAY=":0"

# if ! xrandr --query | grep "1920x1080"; then
#   xrandr --newmode "1920x1080" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync
#   xrandr --addmode DP1 "1920x1080"
#   xrandr --output DP1 --mode "1920x1080"
# fi

# Keybord (Shortcut) Setup
sxhkd -c "$HOME"/.config/bspwm/sxhkdrc &

# Setup Compositer
picom --config "$HOME"/.config/bspwm/picom.conf &

# Notification Setup
bspdunst

# Autolock
xss-lock -- betterlockscreen -l &

# Restoring colorscheme
wal -R

# Starting bspwm
exec bspwm
