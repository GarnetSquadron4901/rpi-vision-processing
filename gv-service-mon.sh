#!/bin/bash

while (1); do
	if ((ps -a | grep mjpg_streamer) && (ps -a | grep java)); then 
		echo good 
	else 
		echo bad
	fi
	sleep 1

done
