### Para dar flash no seu ESP8266 rode:

sudo python esptool.py -p /dev/cu.usbserial-DA01OL9O --baud 115200 write_flash 0x00000 ~/Downloads/esp8266-2016-06-03-v1.8.1.bin
