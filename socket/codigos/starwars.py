# Conecto a um WiFi para poder liberar o acesso a internet do MicroPython
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.scan()
sta_if.connect("<AP_name>", "<password>")
sta_if.isconnected()
# Abro o socket e inicio uma conexão com o server ASCII de Star Wars

import socket
addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
addr = addr_info[0][-1]
s = socket.socket()
s.connect(addr)
while True:
  data = s.recv(500)
  print(str(data, 'utf8'), end='')
