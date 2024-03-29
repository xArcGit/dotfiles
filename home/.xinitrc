#!/usr/bin/env zsh

# Loading Scripts
PATH="$HOME/.config/bspwm/scripts:$PATH"

# Add Rule's to bspwm window
bspc config external_rules_command 		"$HOME"/.config/bspwm/scripts/bspexternalrules

xrandr --output "DP1" --mode "1920x1080"

# Keybord (Shortcut) Setup
sxhkd -c "$HOME"/.config/bspwm/sxhkdrc &

# Setup Compositer
picom --config "$HOME"/.config/bspwm/picom.conf &

# Notification Setup
bspdunst

# Autolock
xss-lock -- betterlockscreen -l &

# Ibus daemon
ibus-daemon -drx &

# Polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Wallpaper Setup 
feh --bg-fill "$(< "${HOME}/.cache/wal/wal")"  

# Restoring colorscheme 
wal -R

# Starting bspwm
exec bspwm
