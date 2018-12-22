#!/bin/bash

# tell it where the Gstreamer libraries are located

export GST_PLUGIN_PATH=/usr/local/lib/gstreamer-0.10
sleep .1

# set some shortcuts to use in the commands file

#export VOICE="/usr/bin/festival --tts"
export VOICE="/usr/bin/flite"
#export VOICE="/usr/bin/espeak"
sleep .1
export PLUGINS="/home/$USER/blather/config/plugins"
sleep .1
export CONFIGDIR="/home/$USER/blather/config"
sleep .1
export CLIP="/home/$USER/.local/share/clipit/history"
sleep .1
# export KEYPRESS="xvkbd -xsendevent -secure -text"
export KEYPRESS="xdotool key"
sleep .1
export KEYHOLD="xdotool keydown"
sleep .1
export KEYTYPE="xdotool type"
sleep .1
export MMOVE="xdotool mousemove"
# XCOORD:YCOORD
sleep .1
export CLICK="xdotool click"
# Generally, left = 1, middle = 2, right = 3, wheel up = 4, wheel down = 5
sleep .1
export BROWSER="firefox"
sleep .1
export CHBROWSER="google-chrome"
sleep .1
export CRMBROWSER="chromium-browser"
sleep .1
export EDITOR="geany"
#export EDITOR="atom"
sleep .1
export FM="pcmanfm"
#export FM="thunar"
sleep .3

# start blather in continuous mode with the GTK GUI
# and a history of 20 recent commands
/home/$USER/blather/./language_updater.sh
python2 /home/$USER/blather/Blather.py
