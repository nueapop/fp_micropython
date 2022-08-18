import time
import machine
import adafruit_mlx90640

machine.freq(240000000)
mlx = adafruit_mlx90640.MLX90640(machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21), freq=400000))
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
frame = [0] * 768
time.sleep(1)

while True:
    try:
        mlx.getFrame(frame)
        print(frame)

    except:
        machine.reset()

    time.sleep(1)