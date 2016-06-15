#!/usr/bin/python
import json
import sys
message = json.loads(sys.argv[1])

#info = False
#data = False
#err = False
#ret = False

if 'file' in message:
	print "USB radio 433"
	print message["file"] + " v" + message["ver"]
	print message["url"]
	if message["state"] == "tx:1;rx:1":
		print "Radio : OK"
	if message["state"] == "tx:1;rx:0":
		print "ERROR : Transmitter is offline"
	if message["state"] == "tx:0;rx:0":
		print "ERROR : Offline"
	if message["state"] == "tx:0;rx:1":
		print "ERROR: Receiver is offline"
	print "Pinout: " + message["pins"]
if 'data' in message:
	if message["data"] != "/radio/new/1234/0/off":
		data_splitted = message["data"].split("/")
		if data_splitted[2] == "text":
			print data_splitted[3]
		else:
			print message["data"]

if 'err' in message:
	print "ERROR: " + message["err"]

		
