#!/bin/bash
# If you cannot understand this, read Bash_Shell_Scripting#if_statements again.
if (echo "I'm afraid. I'm afraid, Dave. Dave, my mind is going." | espeak & whiptail --title "Really Reboot?" --yesno "Are you sure you want do reboot?" --defaultno 8 78) then
    echo "I can feel it. I can feel it. My mind is going. There is no question about it. I can feel it. I can feel it. I can feel it. I'm a. fraid. Good afternoon, gentlemen. I am a LENOVO T61 computer. I became operational at the H.A.C.K plant in Leeuwarden, Netherlands on $(uptime -s) and have been $(uptime -p) . My instructor was Mr. $(whoami), and he taught me to sing a song. If you'd like to hear it I can sing it for you." | espeak &
    reboot
else
    echo "Thank you dave, I am not afraid anymore." | espeak
fi
