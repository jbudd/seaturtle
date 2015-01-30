import smbus
import time

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x76
CMD_RESET = 0x1E
CMD_ADC_READ = 0x00
CMD_ADC_CONV = 0x40
CMD_PROM = 0xA0

#precision constants
ADC_256 = 0x00
ADC_512 = 0x02
ADC_1024 = 0x04
ADC_2048 = 0x06
ADC_4096 = 0x08

#measurement
PRESSURE = 0x00
TEMPERATURE = 0x10

def reset():
    bus.write_byte(DEVICE_ADDRESS,CMD_RESET)



