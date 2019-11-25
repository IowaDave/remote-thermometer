#!/usr/bin/python3
#
# setup
#
# import needed modules
import serial
import time
import os
# connection object to Arduino serial port
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# variables for scheduling
lastMeasurement = time.localtime()[3]
lastUpload = time.localtime()[3]
#
# loop
#
while 1:
    # poll the Arduino serial port
    # and decode any received bytes into text
    t = ser.readline().decode('utf-8')
    if t != '':  # t is not blank, so process the text
        timeStruct = time.localtime() # a list of time-related numbers
        # update the list of temperatures each time the hour changes by 1
        if timeStruct[3] != lastMeasurement: # the hour has changed
            print('Time:',time.asctime(timeStruct),'Temp:',t.rstrip()) # first, print to the console
            # then, write to the temperatures file
            with open('/home/pi/Documents/Temperduino/temperatures.txt', 
            mode='a', encoding='utf-8') as theFile:
                theFile.write('Time: ')
                theFile.write(time.asctime(timeStruct))
                theFile.write(' Temp: ')
                theFile.write(t.rstrip())
                theFile.write('\n')
                theFile.flush()
            lastMeasurement = timeStruct[3]
        # update the web page at 6 a.m., 2 p.m., and 10 p.m.
        if (((timeStruct[3] == 6) 
            or (timeStruct[3] == 14) 
            or (timeStruct[3] == 22))
            and (timeStruct[3] != lastUpload)):
            # wait a minute for the file flush call to complete
            time.sleep(60)
            # truncate the web page file then start writing to it
            with open('index.html', mode='w') as outFile:
                # start an html5 page
                outFile.write("<html>\n<head>\n")
                outFile.write("<title>Temperatures</title>\n")
                outFile.write("</head>\n<body>\n<p>\n")
                #read the temperature data lines into a list
                with open('temperatures.txt') as inFile:
                    theList = inFile.readlines()
                # reverse the list and write it out with html markup
                theList.reverse()
                for line in theList:
                    outFile.write(line.rstrip())
                    outFile.write("<br>\n")
                # conclude the html file
                outFile.write("</p>\n</body>\n</html>\n")
                outFile.flush()
            # wait a minute for the file flush to finish
            time.sleep(60)
            # call a script to upload index.html to the web server
            os.system('/home/pi/Documents/Temperduino/uploadWebPage.sh')
            lastUpload = timeStruct[3]
    time.sleep(1)
