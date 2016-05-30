#!/bin/bash
kill $(ps aux | grep 'Blather.py' | awk '{print $2}')
