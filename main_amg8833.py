import time
import machine
import adafruit_amg8833

machine.freq(240000000)
i2c = machine.I2C(0, scl=machine.Pin(23), sda=machine.Pin(22), freq=400000)
amg = adafruit_amg8833.AMG8833(i2c, addr=0x69)
time.sleep(1)

while True:
	try:
		print(amg.pixel())
	
	except:
		machine.reset()

	time.sleep(1)