# fp_micropython
> Base on ESP32
## Firmware Download
- [ESP32 Firmware](https://micropython.org/resources/firmware/esp32-20220618-v1.19.1.bin)
## Firmware Installation Instructions
- esptool --chip esp32 --port COM7 erase_flash
- esptool --chip esp32 --port COM7 --baud 460800 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin
#
## License

[GNU](https://github.com/nueapop/fp_micropython/blob/main/LICENSE)
