install-dependencies:
	sudo apt install $(cat "$(dirname "$0")/pkglist.txt")

	# There is not deb package for this module
	sudo pip3 install adafruit-circuitpython-pcd8544 --break-system-packages

install: install-dependencies
	cp rpimonitor.py /usr/local/bin/rpimonitor

	cp -r pcd8544 /usr/lib/python3/dist-packages/
	cp -r rpi_informer /usr/lib/python3/dist-packages/

	cp fonts/* /usr/local/share/fonts/rpimonitor/

	cp rpimonitor.service /etc/systemd/system/

	cp rpimonitor.conf /etc/

uninstall:
	rm /usr/local/bin/rpimonitor

	rm -rf /usr/lib/python3/dist-packages/ pcd8544
	rm -rf /usr/lib/python3/dist-packages/rpi_informer

	rm -rf /usr/local/share/fonts/rpimonitor/

	rm  /etc/systemd/system/rpimonitor.service

	rm /etc/rpimonitor.conf
