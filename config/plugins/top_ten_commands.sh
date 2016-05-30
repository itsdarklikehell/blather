#!/bin/sh
cat ~/.bash_history | tr "\|\;" "\n" | sed -e "s/^ //g" | cut -d " " -f 1 | sort | uniq -c | sort -n | tail -n 15 > ~/.config/blather/data/top_ten_commands.txt
echo "these are your top ten commands:" | espeak
cat ~/.config/blather/data/top_ten_commands.txt &
espeak -f ~/.config/blather/data/top_ten_commands.txt
