#!/usr/bin/python3
#
# Notice the use of full file path names here.
# This is to enforce path certainty when cron runs the program.
# Doing so seems to avoid certain otherwise un-figure-outable problems.
#
# Create an html file from data
# in the temperatures.txt file
# truncate the web page file then start writing to it
with open('/home/pi/Documents/Temperduino/index.html', mode='w') as outFile:
    # start an html5 page
    outFile.write("<html>\n<head>\n")
    outFile.write("<title>Temperatures</title>\n")
    outFile.write("</head>\n<body>\n<p>\n")
    #read the temperature data lines into a list
    with open('/home/pi/Documents/Temperduino/temperatures.txt') as inFile:
        theList = inFile.readlines()
    # reverse the list and write it out with html markup
        theList.reverse()
        for line in theList:
            outFile.write(line.rstrip())
            outFile.write("<br>\n")
        # conclude the html file
        outFile.write("</p>\n</body>\n</html>\n")
        outFile.flush()

