#!/bin/sh
cat ~/.bash_history | tr "\|\;" "\n" | sed -e "s/^ //g" | cut -d " " -f 1 | sort | uniq -c | sort -n | tail -n 15 > ~/blather/config/data/top_ten_commands.txt
echo "these are your top ten commands:" | espeak
cat ~/blather/config/data/top_ten_commands.txt &
espeak -f ~/blather/config/data/top_ten_commands.txt
echo "press [ENTER] to exit . . ."
read enterkey
