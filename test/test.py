#!/usr/bin/python

import serial
import os
serial_speed = 9600

try:
    arduino = serial.Serial("/dev/ttyUSB0", serial_speed, timeout=1)
    print "Try /dev/ttyUSB0"
except:
        arduino = serial.Serial("/dev/ttyUSB1", serial_speed, timeout=1)
        print "Try /dev/ttyUSB1"

arduino.flushInput()
data = ""
current_data = False
wait = 3
try:
    while True:
        try:

            current_data = arduino.readline()
        except:
            print "Close Communication"
            os._exit(1)
        if current_data:
            data += current_data
        else:
            wait = wait - 1
            # print data
            # print "Waiting for "+str(wait)
            if wait == 0:
                print data
                checkData = open('test.txt', 'r').read().find(data)
                if checkData == 0:
                    print "OK"
                    os._exit(0)
                else:
                    print "NOK"
                    os._exit(2)
                # f = open("test.txt","w")
                # f.write(data)
                # f.close()



except KeyboardInterrupt:
    print "Closing Collector : Keyboard Interrupt"
    arduino.close()
    os._exit(1)
