import os
import threading
import json

"""
Start command
"""

def send_data(data, command):
    cmd = command + " " + json.dumps(data)
    print cmd
    os.system(cmd)

def send(command, data):
    sending_thread = threading.Thread(target=send_data, args=(data, command))
    sending_thread.start()
