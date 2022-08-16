import time
import machine
import remote
import adafruit_mlx90640
import adafruit_st7735r

machine.freq(240000000)

mlx = adafruit_mlx90640.MLX90640(machine.I2C(0, scl=machine.Pin(23), sda=machine.Pin(22), freq=400000))
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
tft = adafruit_st7735r.TFT(machine.SPI(2, baudrate=20000000, polarity=0, phase=0, sck=machine.Pin(14), mosi=machine.Pin(13)), 16, 17, 18)
tft.init_7735(adafruit_st7735r.TFT.BLACK)

frame = [0] * 768
time.sleep(1)

def getInfrared():
    for i in range(0, 10):
        mlx.getFrame(frame)
        for h in range(24):
                for w in range(32):
                    t = frame[h * 32 + w]
                    color = int((t-20)/20*255)
                    TFTCOLOR = adafruit_st7735r.TFTColor(color, color, color)

                    if(t < 27.99): TFTCOLOR = adafruit_st7735r.TFTColor(0xEB, 0x83, 0x34)
                    elif(t < 28.51): TFTCOLOR = adafruit_st7735r.TFTColor(0xEB, 0xC3, 0x34)  
                    elif(t < 28.99): TFTCOLOR = adafruit_st7735r.TFTColor(0xE4, 0xEB, 0x34) 
                    elif(t < 29.51): TFTCOLOR = adafruit_st7735r.TFTColor(0xBB, 0xEB, 0x34)
                    elif(t < 29.99): TFTCOLOR = adafruit_st7735r.TFTColor(0xB1, 0xEB, 0x34)
                    elif(t < 30.51): TFTCOLOR = adafruit_st7735r.TFTColor(0x34, 0xEB, 0x6E) 
                    elif(t < 30.99): TFTCOLOR = adafruit_st7735r.TFTColor(0x34, 0xEB, 0xBF) 
                    elif(t < 31.55): TFTCOLOR = adafruit_st7735r.TFTColor(0x34, 0xEB, 0xEB) 
                    elif(t < 31.99): TFTCOLOR = adafruit_st7735r.TFTColor(0x53, 0xD5, 0x53)
                    elif(t < 32.55): TFTCOLOR = adafruit_st7735r.TFTColor(0x34, 0xB1, 0xEB)
                    elif(t < 32.99): TFTCOLOR = adafruit_st7735r.TFTColor(0x34, 0x8E, 0xEB)
                    elif(t < 33.55): TFTCOLOR = adafruit_st7735r.TFTColor(0x34, 0x70, 0xEB)
                    elif(t < 33.55): TFTCOLOR = adafruit_st7735r.TFTColor(0x34, 0x53, 0xEB)
                    elif(t < 33.99): TFTCOLOR = adafruit_st7735r.TFTColor(0x1D, 0x3F, 0xE7)
                    elif(t < 34.55): TFTCOLOR = adafruit_st7735r.TFTColor(0x00, 0x00, 0xFF)
                    elif(t < 34.99): TFTCOLOR = adafruit_st7735r.TFTColor(0xD9, 0x27, 0x27)
                    elif(t > 35.00): TFTCOLOR = adafruit_st7735r.TFTColor(0x02, 0x02, 0xC4) 

                    tft.fillrect((w*4,h*7),(4,7), TFTCOLOR)
        print(frame)
    tft.fill(adafruit_st7735r.TFT.BLACK)

def callback(data, addr, ctrl):
    try:
        if data == 28:
            print('Data {0} Addr {1} Ctrl {2}'.format(data, addr, ctrl))
            getInfrared()
        else:
            print('Data {0} Addr {1} Ctrl {2}'.format(data, addr, ctrl))
            tft.fill(adafruit_st7735r.TFT.BLACK)

    except:
        machine.reset()

remote.NEC_16(machine.Pin(15, machine.Pin.IN), callback)