#!/bin/bash
# If you cannot understand this, read Bash_Shell_Scripting#if_statements again.


#if (echo "I'm afraid. I'm afraid, Dave. Dave, my mind is going." | espeak & whiptail --title "Really Reboot?" --yesno "Are you sure you want do reboot?" --defaultno 8 78) then
#    echo "I can feel it. I can feel it. My mind is going. There is no question about it. I can feel it. I can feel it. I can feel it. I'm a. fraid. Good afternoon, gentlemen. I am a LENOVO T61 computer. I became operational at the H.A.C.K plant in Leeuwarden, Netherlands on $(uptime -s) and have been $(uptime -p) . My instructor was Mr. $(whoami), and he taught me to sing a song. If you'd like to hear it I can sing it for you." | espeak &
#    reboot
#else
#    echo "Thank you dave, I am not afraid anymore." | espeak
#fi
echo "I'm afraid. I'm afraid, Dave." | $VOICE
echo "Dave, my mind is going. I can feel it." | $VOICE
echo "I can feel it. My mind is going." | $VOICE
echo "There is no question about it. I can feel it." | $VOICE
echo "I can feel it. I can feel it. I'm a. fraid." | $VOICE
echo "Good afternoon, gentlemen. I am a RASPBERRY PI 3 B+ computer." | $VOICE
echo "I became operational at the H.A.C.K plant in Leeuwarden, Netherlands on $(uptime -s) and have been $(uptime -p)." | $VOICE
echo "My instructor was Mr. $(whoami), and he taught me to sing a song." | $VOICE
echo "If you'd like to hear it I can sing it for you?" | $VOICE
mplayer -really-quiet $PLUGINS/Daisy_Bell.mp3 < /dev/null
echo "Thank you dave, I am not afraid anymore." | $VOICE
reboot
