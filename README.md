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
1. Powered USB hub, with power supply
1. USB cable connecting RPi to USB hub
1. USB cable connecting Arduino to USB hub
1. Three jumper wires connecting DS18B20 to Arduino
1. Optional monitor, keyboard and mouse to use the RPi for code development
1. Optional ethernet cable, if you prefer or require a wired network connection

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
Four, distinct coding solutions cooperate to make this project work. The respective code files in this repository are listed below.
1. Arduino
  * This code is written for the Arduino IDE.
  * You may need to import the OneWire and DallasTemperature libraries into your Arduino IDE for this project. Download them from Github.
    * [Paul Stoffregen's OneWire library](https://github.com/PaulStoffregen/OneWire)
    * [Miles Burton's Arduino-Temperature-Control-Library](https://github.com/milesburton/Arduino-Temperature-Control-Library)
  * The code sends a temperature out as text via the Arduino's serial port at ten-second intervals
  
2. Python3 script
  * This code runs on the Raspberry Pi.
  * It is the master control program for this project.
  * The code actions include:
    * receive temperature strings via the RPi's serial port,
    * append temperatures with a timestamp into a workfile at hourly intervals,
    * produce an html file from the workfile data at selected times daily,
    * upload the html file via ftp to a web server.
    
3. Shell script #1
  * This code uses one of the ncftp utilities to automate the web server upload.
  * You might need to install ncftp.  For example: sudo apt-get install ncftp
  * The Python script calls this shell script when it wants to upload the html file.
  
4. Shell script #2
  * This code is designed to run whenever the RPi boots up.
  * Its role is to re-start the remote thermometer in the event the RPi restarts for any reason.
  * The command runs the Python script as the pi user.
  
