#!/usr/bin/python3
#
# Read one temperature from Arduino
#
import serial
import time
# connection object
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#
temp = '12.34'  # populate this variable with junk text so it is not blank
#
# Step 1 poll the Arduino repeatedly
# to clear prior temperatures from its output buffer
while temp != '':
    temp = ser.readline().decode('utf-8')
#
# Step 2 poll the Arduino repeatedly
# until it sends the next temperature
while temp == '':
    temp = ser.readline().decode('utf-8')
#
# Step 3 append the temperature
# to the temperatures.txt file
with open('/home/pi/Documents/Temperduino/temperatures.txt', 
    mode='a', encoding='utf-8') as theFile:
    theFile.write('Time: ')
    theFile.write(time.asctime())
    theFile.write(' Temp: ')
    theFile.write(temp.rstrip())
    theFile.write('\n')
    theFile.flush()
    theFile.close()

