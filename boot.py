# boot.py
import network
import utime
import ntptime
from machine import Pin
from time import sleep

#station mode
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    time_out = False
    start_time = utime.time()

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('wifi-name', 'pass')
        while not sta_if.isconnected() and not time_out:
            if utime.time() - start_time >= 10:
                timed_out = True
            else:
                pass

    if sta_if.isconnected():
        for n in range(0,10):
            Pin(14, Pin.OUT).value(0)
            sleep(0.2)
            Pin(14, Pin.OUT).value(1)
            sleep(0.2)
        Pin(14, Pin.OUT).value(0)
        print('network config:', sta_if.ifconfig())
    else:
        for n in range(0,20):
            Pin(14, Pin.OUT).value(0)
            sleep(0.2)
            Pin(14, Pin.OUT).value(1)
            sleep(0.2)
        Pin(14, Pin.OUT).value(1)
        print('disable to connect WiFi')


do_connect()
