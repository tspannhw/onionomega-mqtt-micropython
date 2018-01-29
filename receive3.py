from OmegaExpansion import oledExp
import paho.mqtt.client as client
import time
import os
import datetime
import math
import random, string
import json
import sys
import socket
import json
from time import sleep
from string import Template
from time import gmtime, strftime

# Time
start = time.time()
currenttime= strftime("%Y-%m-%d %H:%M:%S",gmtime())
host = os.uname()[1]
external_IP_and_port = ('198.41.0.4', 53)  # a.root-servers.net
socket_family = socket.AF_INET

def IP_address():
        try:
            s = socket.socket(socket_family, socket.SOCK_DGRAM)
            s.connect(external_IP_and_port)
            answer = s.getsockname()
            s.close()
            return answer[0] if answer else None
        except socket.error:
            return None
ipaddress = IP_address()

status  = oledExp.driverInit()
status = oledExp.setDisplayPower(1)
status = oledExp.scroll (0, 0, 0, 8-1);


endtime= strftime("%Y-%m-%d %H:%M:%S",gmtime())
end = time.time()
row = [ { 'end': str(end), 'endtime': str(endtime), 'ipaddress': str(ipaddress) } ]
json_string = json.dumps(row)
broker="192.168.1.193"
port=1883
client1= client.Client("onion")                           #create client object
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("omega",json_string)

status = oledExp.write(json_string)
print(status)
