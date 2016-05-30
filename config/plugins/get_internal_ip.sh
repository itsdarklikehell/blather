#!/bin/bash
echo "your local ip is" | espeak
ip a s $(ip r s 0/0 | awk '{print $5;exit}') | awk '$1 ~ /inet$/ {print $2;exit}' | espeak
