import machine
import remote

def callback(data, addr, ctrl):
    if data > 0:
        print('Data {0} Addr {1} Ctrl {2}'.format(data, addr, ctrl))

ir = remote.NEC_16(machine.Pin(15, machine.Pin.IN), callback)