#!/usr/bin/env python
#
# Raspberry Pi Rotary Test Encoder Class
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses a standard rotary encoder with push switch
#

import sys
import time
from rotary_class import RotaryEncoder
from socketIO_client import SocketIO, LoggingNamespace

socketIO = SocketIO('localhost', 3000)

play_on = 1 # plays: 1 = play, 0 = pause

# Define GPIO inputs
VOLUME_UP =     23 	#    Clockwise
VOLUME_DOWN =   24	#    Anticlockwise
MUTE_SWITCH =   27	#    Button Down

# This is the event callback routine to handle events
def volume_event(event):
        global volumeknob, play_on
        if event == RotaryEncoder.CLOCKWISE:
                #print("Clockwise")
                # get initial state
                socketIO.emit('volume', '+')
        elif event == RotaryEncoder.ANTICLOCKWISE:
                #print("Anticlockwise")
                socketIO.emit('volume', '-')
        elif event == RotaryEncoder.BUTTONDOWN:
                #print("Button down: toggle pause/play")
                socketIO.emit('toggle')
        elif event == RotaryEncoder.BUTTONUP:
                #print("Button up")
        return

# Define the switch
volumeknob = RotaryEncoder(VOLUME_UP,VOLUME_DOWN,MUTE_SWITCH,volume_event,2)  # 2 = latest RPi Boards as of 2017

while True:
        time.sleep(0.5)
        #print(volumeknob)

