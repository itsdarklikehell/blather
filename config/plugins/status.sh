#!/bin/bash
## pass options to free ##
# free -m -l -t | espeak

## get top process eating memory
# ps auxf | sort -nr -k 4 | espeak
# ps auxf | sort -nr -k 4 | head -10 | espeak

## get top process eating cpu ##
# ps auxf | sort -nr -k 3 | espeak
# ps auxf | sort -nr -k 3 | head -10 | espeak

## Get server cpu info ##
echo "Cpu status" | $VOICE
lscpu
lscpu | $VOICE

## older system use /proc/cpuinfo ##
##less /proc/cpuinfo | espeak

## get GPU ram on desktop / laptop##
echo "video memory is currently" | $VOICE
grep -i --color memory /var/log/Xorg.0.log
grep -i --color memory /var/log/Xorg.0.log | $VOICE
