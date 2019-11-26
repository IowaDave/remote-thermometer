# Remote Thermometer
<h3>Receive temperature readings remotely<br>
via the Web using a Raspberry Pi<br>
an Arduino, and a DS18B20 digital thermometer</h3>

Presenting the equipment and code used for a working digital thermometer that displays temperature readings on a personally-controlled web site.

#### Equipment
1. DS18B20
1. Arduino Uno
1. Raspberry Pi (RPi)
1. Power supply suitable for the RPi
1. USB cable connecting RPi to Arduino
1. Three jumper wires connecting DS18B20 to Arduino
1. Optional battery-enabled backup power supply, highly recommended
1. Optional ethernet cable, if you prefer or require a wired network connection
1. Optional monitor, keyboard, mouse and powered USB hub to use the RPi for code development

#### Assembly
* Connect the DS18B20 to the Arduino
  * First, identify the function of each pin on the device. See the device spec sheet, [here](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf).
  * Hold it with the pins dangling down, and the flat face of the package facing you.
    1. The pin on the left is Pin 1, 'GND', the ground pin.
    2. The pin in the middle is Pin 2, 'DQ', the data pin.
    3. The pin on the right is Pin 3, 'VDD', the power-in pin.
  * Connect Pin 1 to a GND pin on the Arduino.
  * Connect Pin 2 to a data pin on the Arduino.
  * Connect Pin 3 to the 5V power-out pin on the Arduino.
  
* Hook up all the other cables where they obviously go.

#### Code
One code solution runs on the Arduino. The remaining three runs on the RPi. In the spirit of Unix, the RPi code segments:
* are short, 
* perform only one task each, and
* cooperate with the Linux cron scheduler to make this project work. 

The cron scheduler probably has counterparts in other operating systems. I am just a dumb country boy who does not know everything, so you would have to find that out from someone else.  <grin>
 
Cron makes this project robust for system restarts due to power failure. Cron automatically starts on boot, and it activates programs based on actual times obtained from the RPi's real time clock. If the power goes out, nothing's lost. The system will resume its task when the power comes back on. This precaution is in addition to using a battery-enabled backup power supply.

The respective code files in this repository are listed below.
1. Arduino: *thermoduino.ino*
  * This code is written for the Arduino IDE.
  * You may need to import the OneWire and DallasTemperature libraries into your Arduino IDE for this project. Download them from Github.
    * [Paul Stoffregen's OneWire library](https://github.com/PaulStoffregen/OneWire)
    * [Miles Burton's Arduino-Temperature-Control-Library](https://github.com/milesburton/Arduino-Temperature-Control-Library)
  * The code sends a temperature out as text via the Arduino's serial port at ten-second intervals
  
2. Python3 script: *readTemperature.py*
  * This code runs on the Raspberry Pi.
  * Its job is to fetch a temperature from the Arduino and append it to a data accumulation file.
  * It closes the file and exits immediately after each temperature reading.
  * Cron runs it once at the beginning of each hour.
    
3. Python3 script: *createTempsHomePage.py*
  * Cron runs it on the RPi once, at 5 minutes past the hour, at four-hour intervals
  * Reads the entire data accumulation file into a list (see #2, above)
  * Reverses the list, placing most recent data first.
  * Writes the list out as an 'index.html' file, that is, a web page file.
 
4. Shell script #1: *uploadWebPage.sh*
  * Cron runs this code runs on the RPi about 5 minutes after the index.html file is updated.
  * The script uses one of the ncftp utilities to automate the web server upload.
  * You might need to install ncftp.  For example: sudo apt-get install ncftp
  * The Python script calls this shell script when it wants to upload the html file.
  * Modify the command to use the ftp credentials and ip address for your personal web server.
  
