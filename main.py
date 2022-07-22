import machine
import gc
import time
from machine import I2C, Pin, SPI
import adafruit_mlx90640
from ST7735 import TFT, TFTColor
import math
import network, socket
from random import randint

machine.freq(240000000)
gc.collect()

#hardware SPI, HSPI
spi = SPI(1, baudrate=8000000, polarity=0, phase=0)
# dc, rst, cs
tft=TFT(spi,16)
tft.init_7735(tft.BLACKTAB)
# blue, green, red
# #50C7C7 ---> 0xC7, 0xC7, 0x50
tft.fill(TFTColor(0xEB, 0x83, 0x34))

i2c = I2C(0, scl=Pin(22, Pin.OUT), sda=Pin(21, Pin.OUT), freq=400000)
mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C")
print([hex(i) for i in mlx.serial_number])

mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

frame = [0] * 768

gc.collect()
time.sleep(0.5)
print('starting ...')

while True:

    rect_hig = 6
    rect_wid = 4
    pixel = 0

    try:
        mlx.getFrame(frame) # read MLX temperatures into frame var

        for h in range(24):
            for w in range(32):
                t = frame[h * 32 + w]

                color = int((t-20)/20*255)
                TFTCOLOR = TFTColor(color, color, color)

                if(t < 27.99): TFTCOLOR = TFTColor(0xEB, 0x83, 0x34)
                elif(t < 28.51): TFTCOLOR = TFTColor(0xEB, 0xC3, 0x34)  
                elif(t < 28.99): TFTCOLOR = TFTColor(0xE4, 0xEB, 0x34) 
                elif(t < 29.51): TFTCOLOR = TFTColor(0xBB, 0xEB, 0x34)
                elif(t < 29.99): TFTCOLOR = TFTColor(0xB1, 0xEB, 0x34)
                elif(t < 30.51): TFTCOLOR = TFTColor(0x34, 0xEB, 0x6E) 
                elif(t < 30.99): TFTCOLOR = TFTColor(0x34, 0xEB, 0xBF) 
                elif(t < 31.55): TFTCOLOR = TFTColor(0x34, 0xEB, 0xEB) 
                elif(t < 31.99): TFTCOLOR = TFTColor(0x53, 0xD5, 0x53)
                elif(t < 32.55): TFTCOLOR = TFTColor(0x34, 0xB1, 0xEB)
                elif(t < 32.99): TFTCOLOR = TFTColor(0x34, 0x8E, 0xEB)
                elif(t < 33.55): TFTCOLOR = TFTColor(0x34, 0x70, 0xEB)
                elif(t < 33.55): TFTCOLOR = TFTColor(0x34, 0x53, 0xEB)
                elif(t < 33.99): TFTCOLOR = TFTColor(0x1D, 0x3F, 0xE7)
                elif(t < 34.55): TFTCOLOR = TFTColor(0x00, 0x00, 0xFF)
                elif(t < 34.99): TFTCOLOR = TFTColor(0xD9, 0x27, 0x27)
                elif(t > 35.00): TFTCOLOR = TFTColor(0x02, 0x02, 0xC4) 

                tft.fillrect((w*rect_wid,h*rect_hig),(rect_wid,rect_hig), TFTCOLOR)

        print(frame)
        print("finish")  

    except:
        machine.reset()
    
    time.sleep(0.5)