#!/bin/bash

while true
do
	if ((ps -a | grep mjpg_streamer) && (ps -a | grep java)); then 
		python ~/leds/clear_error.py
	else 
		python ~/leds/set_error.py
	fi
	sleep 1

done
