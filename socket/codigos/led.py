import machine
from time import sleep

led_pin = machine.Pin(2, machine.Pin.OUT)  # Defino o Loop 

while True:
  led_pin.high()
  sleep(1)
  led_pin.low()
  sleep(1)
