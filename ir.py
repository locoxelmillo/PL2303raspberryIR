import RPi.GPIO as GPIO
import time
import serial

#Configuration GPIO of RaspberryPI3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

#Configuration initial port Serial
ser = serial.Serial(
    port = '/dev/ttyUSB0',             #Position initial port USB
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

#Channel
CH5   = "\xAA\xA7\xBF\x05"  #Code channel 5
CH3   = "\xAA\xA7\xBF\x03"  #Code channel 3
AV    = "\xAA\xA7\xFC\x05"  #Code AV
HDMI  = "\xAA\xA7\xFC\x52"  #Code change channel HDMI
HDMI1 = "\xAA\xA7\x0F\x0F"  #Code HDMI1
HDMI2 = "\xAA\xA7\x0F\x00"  #Code HDMI2
HDMI3 = "\xAA\xA7\xBF\x03"  #Code HDMI3
ATV   = "\xAA\xA7\xBF\x1B"  #Code ATV
DTV   = "\xAA\xA7\xF4\x0B"  #Code DTV
data1 = AV                  #Variable1 reemplace
data2 = ATV                 #Variable2 reemplace
data3 = HDMI                #Variable3 reemplace


while 1:
        if GPIO.input(4)==1:
            print("AV")              #test witness
            ser.write(data1)
            time.sleep(0.5)
            ser.write(data2)
            time.sleep(0.5)        
            time.sleep(5)
        
        
        

