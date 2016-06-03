#!/bin/bash
echo "What time are you setting this alarm for? " &&
echo "What time are you setting this alarm for? " | espeak &&
read date
echo Okay! Will ring you on $(date --date="$date").
echo Okay! Will ring you on $(date --date="$date"). | espeak &&
sleep $(( $(date --date="$date" +%s) - $(date +%s) ));
echo Wake up!
echo Wake up! | espeak
while true; do
	xdotool key XF86AudioRaiseVolume
	amixer set Master 100%
	/usr/bin/mpg123 --quiet -@ http://icecast.omroep.nl/3fm-bb-mp3.m3u
  exit 1
done
