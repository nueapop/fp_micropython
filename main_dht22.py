import time
import machine
import dht

sensor = dht.DHT22(machine.Pin(4))
time.sleep(1)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)

    except OSError as e:
        print('Failed to read sensor.')

    time.sleep(1)