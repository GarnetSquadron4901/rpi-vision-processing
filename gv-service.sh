if [ps -a | grep pyro4-ns] || [ps -a | grep mjpg-streamer] || [ps -a | grep java] || [ps -a | grep python]; then
	echo Garnet Vision process already running. Aborting.
	exit
fi

./start_all.sh &

python wait_for_shutdown.py

./stop_all.sh
sudo poweroff
