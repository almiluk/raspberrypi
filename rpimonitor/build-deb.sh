set -e

readonly prefix=debian/tmp/

mkdir -p $prefix/debian
find debian -maxdepth 1 -type f | xargs -I {} cp {} $prefix/debian
#cp debian/(*.*) debian/debian/DEBIAN

mkdir -p $prefix/usr/local/bin
cp rpimonitor.py $prefix/usr/local/bin/

mkdir -p $prefix/usr/lib/python3/dist-packages
cp -r pcd8544 $prefix/usr/lib/python3/dist-packages/
cp -r rpi_informer $prefix/usr/lib/python3/dist-packages/

mkdir -p $prefix/usr/local/share/fonts/rpimonitor
cp fonts/* $prefix/usr/local/share/fonts/rpimonitor/

mkdir -p $prefix/etc/systemd/system
cp rpimonitor.service $prefix/etc/systemd/system/


cd $prefix
dpkg-buildpackage -rfakeroot -uc -us -tc

