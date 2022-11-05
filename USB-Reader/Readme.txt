Installed pyserial library for Python->https://pyserial.readthedocs.io/en/latest/pyserial.html#installation
Installed setSerial Linux command to check the ports in use -> https://www.cyberciti.biz/faq/find-out-linux-serial-ports-with-setserial/#:~:text=Use%20the%20setserial%20command%20to,associated%20with%20a%20serial%20port.
Get USB Port details - > lsusb -D /dev/bus/usb/001/005

TASK-> Inorder to set-up the receiver (FT232 USB-Serial (UART) IC) first scan all USB ports and see in which port the device with idProduct matches FT232 USB-Serial (UART) IC.

Install mosquitto broker ->  https://www.vultr.com/docs/install-mosquitto-mqtt-broker-on-ubuntu-20-04-server/
Install python library to interact with Mosquitto broker
Interact with Mosquitto, Tutorial -> https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4
