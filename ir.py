import RPi.GPIO as GPIO
import time
import serial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

CH5   = "\xAA\xA7\xBF\x05"
CH3   = "\xAA\xA7\xBF\x03"
AV    = "\xAA\xA7\xFC\x05"
HDMI  = "\xAA\xA7\xFC\x52"
HDMI1 = "\xAA\xA7\x0F\x0F"
HDMI2 = "\xAA\xA7\x0F\x00"
HDMI3 = "\xAA\xA7\xBF\x03"
ATV   = "\xAA\xA7\xBF\x1B"
DTV   = "\xAA\xA7\xF4\x0B"
data1 = AV
data2 = ATV
data3 = HDMI


while 1:
        if GPIO.input(4)==1:
            print("AV")
            ser.write(data1)
            time.sleep(0.5)
            ser.write(data1)
            time.sleep(0.5)        
            time.sleep(5)
        
        
        
        
        
        # print("ATV")
        # ser.write(data2)
        # time.sleep(0.5)
        # ser.write(data2)
        # time.sleep(0.5)        
        # time.sleep(5)
        # print("HDMI")
        # ser.write(data3)
        # time.sleep(0.5)
        # ser.write(data3)
        # time.sleep(0.5)        
        
        
        
        # if GPIO.input(4)==1:
            # print("Sensor on PRENDIDO")
            # ser.write(data1)
            # time.sleep(0.5)
            # ser.write(data1)
            # time.sleep(0.5)
        # elif GPIO.input(4)==0:
            # print("Sensor off")
            # ser.write(data2)
            # time.sleep(0.5)
            # ser.write(data2)
            # time.sleep(0.5)

