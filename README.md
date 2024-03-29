# fp_micropython
> Base on ESP32
## Hardware Requirements
- [Adafruit MLX90640](https://www.adafruit.com/product/4407)
- [Adafruit AMG8833](https://www.adafruit.com/product/3538)
- [MicroSD Card Adapter]()
- [DHT22]()
- [KY-022]()
- [IR Transmitter]()
- [Adafruit ST7735R](https://www.adafruit.com/product/358)
- [SCT013]() ( Fix Library )
- [Infrared Remote Control]()
## Firmware Download
- [ESP32 Firmware](https://micropython.org/resources/firmware/esp32-20220618-v1.19.1.bin)
## Firmware Installation Instructions
- esptool --chip esp32 --port COM7 erase_flash
- esptool --chip esp32 --port COM7 --baud 460800 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin
## Schematic
![](https://raw.githubusercontent.com/nueapop/fp_micropython/main/assets/images/schematic.png)
### Sensor Wire
- Adafruit MLX90640:
  - VIN: +5V
  - 3VO: X
  - GND: GND
  - SCL: D22
  - SDA: D21

- MicroSD Card Adapter:
  - CS: D5
  - SCK: D18
  - MOSI: D23
  - MISO: D19
  - VCC: +5V
  - GND: GND

- DHT22:
  - VCC: +5V
  - DATA: RX0
  - GND: GND

- KY-022:
  - OUT: D35
  - VCC: +5V
  - GND: GND

- IR Transmitter:
  - DATA: TX2
  - GND: GND

- Adafruit ST7735R:
  - BACKLIGHT: 3V3
  - MISO: X
  - SCK: D33
  - MOSI: D32
  - TFTCS: GND
  - SDCS: X
  - D/C: RX2
  - RST: EN
  - VCC: 3V3
  - GND: GND
#
## License

[GNU](https://github.com/nueapop/fp_micropython/blob/main/LICENSE)
