env LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH mjpg_streamer -o "output_http.so -w ./www -p 1180" -i "input_raspicam.so -fps 30 -x 320 -y 240" &
