#!/usr/bin/python
from lib import Socket
from lib import Command
from lib import Lock
import sys
import time
import os
import serial
import json
import string


""" Main Program """

""" Variables """
timeout = 3
time_end = 0
last_data = ""
lock = False
data = ""

# Get port
with open('/user/config/radio2serial/port', 'r') as port_file:
    content = port_file.read()
    socket_port = int(content.strip())

# Get configuration
with open('/user/config/radio2serial/radio2serial.json') as settings_file:
    settings = json.load(settings_file)

serial_port = settings["port"]
serial_speed = int(settings["speed"])
command = settings["command"]

Socket.Start(socket_port)

"""
Json (to move to JsonParser)
"""


def is_json(jsonLine):
    try:
        json_object = json.loads(jsonLine)
    except ValueError, e:
        return False
    return True

"""
Serial
"""
try:
    arduino = serial.Serial(serial_port, serial_speed, timeout=1)
except:
    print "Serial connection failed"
    print "speed:" + serial_speed
    print "port:" + serial_port
    os._exit(12)
# Flush Buffer
arduino.flushInput()

print "Serial:"+str(serial_port)

try:
    while True:
        data = False
        try:
            data = arduino.readline().strip()
            message = Socket.Listen()
        except:
            print "Close Communication : Serial Communication failure"
            os._exit(2)

        if message is not False:
            # print "Founded something to tell to the arduino"
            # print message
            arduino.write(message + "\n")

        if is_json(data):
            #json_object = json.loads(data)
            #if 'data' in json_object:
            # dataRaw = json_object
            if data == last_data:
                lock = Lock.check(timeout, time_end)
                time_end = lock[0]
                lock = lock[1]
                #print "BLOCKED------"
                ##print "LAST:" + str(last_data)
                ##print "NEW:" + str(data)
                #print "BLOCKED------"
            else:
                lock = False

            if lock is False:
                last_data = data
                print "Serial:"+str(data)
                Command.send(command, data)
                Socket.Send(data)
                data = False

except KeyboardInterrupt:
    print "Closing Collector : Keyboard Interrupt"
    # server_socket.close()
    arduino.close()
    os._exit(13)
