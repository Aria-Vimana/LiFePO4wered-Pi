# LiFePO4wered access Python module
# Copyright (c) 2017 Patrick Van Oosterwijck

from ctypes import cdll


# Variable definitions

I2C_REG_VER           = 0
I2C_ADDRESS           = 1
LED_STATE             = 2
TOUCH_STATE           = 3
TOUCH_CAP_CYCLES      = 4
TOUCH_THRESHOLD       = 5
TOUCH_HYSTERESIS      = 6
DCO_RSEL              = 7
DCO_DCOMOD            = 8
VIN                   = 9
VBAT                  = 10
VOUT                  = 11
IOUT                  = 12
VBAT_MIN              = 13
VBAT_SHDN             = 14
VBAT_BOOT             = 15
VOUT_MAX              = 16
VIN_THRESHOLD         = 17
IOUT_SHDN_THRESHOLD   = 18
VOFFSET_ADC           = 19
VBAT_OFFSET           = 20
VOUT_OFFSET           = 21
VIN_OFFSET            = 22
IOUT_OFFSET           = 23
AUTO_BOOT             = 24
WAKE_TIME             = 25
SHDN_DELAY            = 26
AUTO_SHDN_TIME        = 27
PI_BOOT_TO            = 28
PI_SHDN_TO            = 29
RTC_TIME              = 30
RTC_WAKE_TIME         = 31
PI_RUNNING            = 32
CFG_WRITE             = 33

# Touch states and masks

TOUCH_INACTIVE        = 0x00
TOUCH_START           = 0x03
TOUCH_STOP            = 0x0C
TOUCH_HELD            = 0x0F
TOUCH_ACTIVE_MASK     = 0x03
TOUCH_MASK            = 0x0F

# LED states when Pi on

LED_STATE_OFF         = 0x00
LED_STATE_ON          = 0x01
LED_STATE_PULSING     = 0x02
LED_STATE_FLASHING    = 0x03

# Auto boot settings

AUTO_BOOT_OFF         = 0x00
AUTO_BOOT_VBAT        = 0x01
AUTO_BOOT_VBAT_SMART  = 0x02
AUTO_BOOT_VIN         = 0x03
AUTO_BOOT_VIN_SMART   = 0x04

# Register access masks

ACCESS_READ           = 0x01
ACCESS_WRITE          = 0x02


# Load shared object

lib = cdll.LoadLibrary('/usr/local/lib/liblifepo4wered.so')

# Determine if the specified variable can be accessed in the specified
# manner (read, write or both)

def access_lifepo4wered(var, access_mask):
  return lib.access_lifepo4wered(var, mask)

# Read data from LiFePO4wered device

def read_lifepo4wered(var):
  return lib.read_lifepo4wered(var)

# Write data to LiFePO4wered device

def write_lifepo4wered(var, value):
  return lib.write_lifepo4wered(var, value)

