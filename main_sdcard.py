import os
import time
import machine
import sdcard

sd = sdcard.SDCard(machine.SPI(1, sck=machine.Pin(18), mosi=machine.Pin(23), miso=machine.Pin(19)), machine.Pin(5))
time.sleep(1)

os.mount(os.VfsFat(sd), '/sd')
print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')
print('SD Card contains:{}'.format(os.listdir()))