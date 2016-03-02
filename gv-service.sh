if sudo ps | grep pyro4-ns; then
	exit
fi

./start_all.sh

python wait_for_shutdown.py

./stop_all.sh
sudo poweroff