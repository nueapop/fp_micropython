import machine
import adafruit_st7735r

tft = adafruit_st7735r.TFT(machine.SPI(2, baudrate=20000000, polarity=0, phase=0, sck=machine.Pin(14), mosi=machine.Pin(13)), 16, 17, 18)
tft.init_7735(adafruit_st7735r.TFT.BLACK)
tft.fill(adafruit_st7735r.TFT.RED)