import datetime

import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "localhost"
client = mqtt.Client("faketempclient")
client.connect(mqttBroker,port=1883)

while True:
    x=datetime.datetime.now()
    randNumber = randrange(20,30)
    client.publish("heater/globaltemp", randNumber)
    client.publish("heater/publishedtime",x.strftime("%H:%M:%S  "))
    print(x.strftime("%H:%M:%S  ")+ str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(20)