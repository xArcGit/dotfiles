!/usr/bin/env zsh

# if adb devices | grep b0e7f0e2 > /dev/null; then
#   xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
#   xrandr --addmode "Screen 0" 1920x1080_60
#   xrandr --verbose --output DP1 --primary
#   xrandr --output "Screen 0" --mode 1920x1080_60 --left-of DP-1
#   x11vnc -clip 1920x1080_60+0+0 -nocuck123
#   rsorshape -nocursorpos &
#   x11vnc -usepw &
#   adb reverse tcp:5900 tcp:5901
# fi

# Starting bspwm
exec bspwm
