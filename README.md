# fp_micropython
> Base on ESP32
## Hardware Requirements
- [Adafruit MLX90640](https://www.adafruit.com/product/4407) ( Used )
- [Adafruit AMG8833](https://www.adafruit.com/product/3538)
- [MicroSD Card Adapter]()
- [DHT22]()
- [KY-022]()
- [IR Transmitter]()
- [Adafruit ST7735R](https://www.adafruit.com/product/358) ( Used )
- [SCT013]() ( Fix Library )
- [Infrared Remote Control]() ( Used )
## Firmware Download
- [ESP32 Firmware](https://micropython.org/resources/firmware/esp32-20220618-v1.19.1.bin)
## Firmware Installation Instructions
- esptool --chip esp32 --port COM7 erase_flash
- esptool --chip esp32 --port COM7 --baud 460800 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin
#
## License

[GNU](https://github.com/nueapop/fp_micropython/blob/main/LICENSE)
