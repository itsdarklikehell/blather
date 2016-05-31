#!/bin/bash
echo "going away now, goodbye cruel world!" | $VOICE
kill $(ps aux | grep 'Blather.py' | awk '{print $2}')
