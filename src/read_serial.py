#!/usr/bin/env python

import serial
import sys


if len(sys.argv) != 2:
    sys.exit(1)
else:
    file_ = sys.argv[1]

port = '/dev/tty.usbserial-A700dEwk'

ser = serial.Serial(port, 9600)

loop = True

lines = []
while loop:
    try:
        line = ser.readline()
        lines.append(line)
        print line.strip()


    except KeyboardInterrupt:
        print "Caught KeyboardInterrupt, terminating reading from serial"
        loop = False

f = open(file_,  'w')
f.writelines(lines)
f.close()
