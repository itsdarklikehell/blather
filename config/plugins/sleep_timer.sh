#!/bin/bash
echo "What time are you setting this sleep timer for? " &&
echo "What time are you setting this sleep timer for? " | espeak &&
read date
echo Okay! I Will mute all sound on $(date --date="$date").
echo Okay! I Will mute all sound on $(date --date="$date"). | espeak &&
sleep $(( $(date --date="$date" +%s) - $(date +%s) ));
echo Going to sleep now!
echo Going to sleep now! | espeak
while true; do
	amixer set Master 0% & xdotool key XF86AudioMute
	exit 1
done
