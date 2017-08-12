#!./bin/python

import paho.mqtt.client as mqtt

from ouimeaux.environment import Environment

def on_switch(switch):
  print(switch.name)

env = Environment(on_switch)

env.start()

env.discover(seconds=3)

def on_connect(client, userdata, flags, rc):
  print ("Connected with result code {}".format(rc))
  client.subscribe("gordon/smarthouse/wemo/+")

def on_message(cleint, userdata, msg):
  switch = msg.topic.split('/')[-1]
  try:
    state = int(msg.payload.decode('utf-8'))
    wemo_switch = env.get_switch(switch)
    wemo_switch.basicevent.SetBinaryState(BinaryState=state)
  except:
    pass
  print ("Got request to set state of switch {} to {}".format(switch, msg.payload.decode('utf-8')))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.bluesmoke.network", 1883, 60)

client.loop_forever()
