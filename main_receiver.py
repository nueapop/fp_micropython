import machine
import ir_receiver

def callback(data, addr, ctrl):
    if data > 0:
        print('Data 0x{:02x} Addr 0x{:04x}'.format(data, addr))

ir = ir_receiver.NEC_16(machine.Pin(15, machine.Pin.IN), callback)