import machine
from ir_transmitter.ir_transmitter import irSelectCMD, irSendCMD

irLedPwmObject = machine.PWM(machine.Pin(2, machine.Pin.OUT), freq=38000, duty=0)
irCMDList = irSelectCMD(0)
irSendCMD(irLedPwmObject, irCMDList, duty=360)
print(irCMDList)