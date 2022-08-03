import time
from machine import Pin
from ir_receiver import NEC_16

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        print('Data 0x{:02x} Addr 0x{:04x}'.format(data, addr))

ir = NEC_16(Pin(15, Pin.IN), callback)