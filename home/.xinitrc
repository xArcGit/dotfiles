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

# if adb devices | grep b0e7f0e2 > /dev/null; then
#   xrandr --newmode "1920x1080"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
#   xrandr --addmode VIRTUAL1 1920x1080
#   xrandr --verbose --output DP1 --primary
#   xrandr --output VIRTUAL1 --mode 1920x1080 --left-of DP1
#   x11vnc -clip 1920x1080+0+0 -nocursorshape -nocursorpos &
#   x11vnc -usepw &
#   adb reverse tcp:5900 tcp:5901
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
