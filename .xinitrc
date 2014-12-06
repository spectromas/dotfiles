#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

# Configuration
xrdb -merge ~/.Xresources

if [ -s ~/.Xmodmap ]; then
    xmodmap ~/.Xmodmap
fi

# Daemons
spacefm -d &
(sleep 1 && cadence-session-start -s) &
udevil &

# Programs
# urxvtd -q -o -f &
(sleep 1 && compton --opengl) &
(sleep 2 && mpd) &
# (sleep 2 && unclutter) &
(sleep 3 && parcellite -n) &
(sleep 3 && redshift) &
(sleep 10 && qbittorrent) &

# Window Manager
exec dbus-launch --sh-syntax --exit-with-session awesome
#sxhkd & exec dbus-launch --sh-syntax --exit-with-session bspwm
