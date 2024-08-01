from setuptools import setup
from glob import glob


setup(
    name="rpimonitor",  # the name of the deb package
    version="0.1",  # version
    author="almiluk",  # your name
    maintainer="almiluk",
    author_email="almiluk@gmail.com",  # your email
    description="The program, reading RaspberryPi sensors and perform some actions based on that, e.g. shows it on pcd8544 display",  # description
    long_description="The program, reading RaspberryPi sensors and perform some actions based on that, e.g. shows it on pcd8544 display",
    scripts=["rpimonitor.py"],  # the main script
    data_files=[
        ("/etc/systemd/system", ["rpimonitor.service"]),
        ("/usr/share/fonts/rpimonitor", glob("fonts/*")),
        ("/usr/lib/python3/dist-packages/rpi_informer", glob("rpi_informer/*")),
        ("/usr/lib/python3/dist-packages/pcd8544", glob("pcd8544/*"))
    ],
    install_requires=[
        "psutil", "adafruit-circuitpython-pcd8544", "Pillow", "RPi-GPIO", "gpiod"
    ],  # dependencies
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    py_modules=[],
)
