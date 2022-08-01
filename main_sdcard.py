import os
import time
import machine
import sdcard

sd = sdcard.SDCard(machine.SPI(1, sck=machine.Pin(18), mosi=machine.Pin(19), miso=machine.Pin(21)), machine.Pin(5))
time.sleep(1)