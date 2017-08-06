#!/bin/bash
# echo "Sorry sir, I could not understand you." | espeak
echo "$(shuf -n1 $CONFIGDIR/data/invalid_command.txt)" | $VOICE
