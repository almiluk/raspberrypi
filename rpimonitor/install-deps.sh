sudo apt install $(cat "$(dirname "$0")/pkglist.txt")

sudo pip3 install adafruit-circuitpython-pcd8544 --break-system-packages

#sudo chown root.gpio /dev/gpiomem
#sudo chmod g+rw /dev/gpiomem
