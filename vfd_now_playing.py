#!/usr/bin/env python
# https://volumio.org/forum/gpio-pins-control-volume-t2219.html
# https://pypi.python.org/pypi/socketIO-client
# https://volumio.github.io/docs/API/WebSocket_APIs.html

import time
from time import sleep
import subprocess
from socketIO_client import SocketIO, LoggingNamespace
import spidev
import VFD

socketIO = SocketIO('localhost', 3000)
status = 'play'

artist = ""
title = ""
album = ""
prev_artist = ""
prev_title = ""


# initalize SPI
vfd=VFD.SPI()

vfd.init_VFD()

def display():
    vfd.blank_lines()
    sleep (0.1)

    vfd.setCursor(0,0)
    vfd.text(artist)
    vfd.setCursor(0,1)
    vfd.text(title)

def on_push_state(*args):
# print('state', args)
    global status, artist, title, prev_artist, prev_title
    status = args[0]['status'].encode('ascii', 'ignore')
    
    if status == "stop":
       artist = " Currently Stopped   "
       title  = " "
       display()
       return
     
    artist = args[0]['artist'].encode('ascii', 'ignore')
   
    title  = args[0]['title'].encode('ascii', 'ignore')
 
    #print status               
    #print artist, title

    if artist == prev_artist:
        pass
    else:
        print("Artist: ", artist)
        prev_artist = artist
        display()

    if title == prev_title:
        pass
    else:
        print("Title: ", title)
        prev_title = title
        display()
        
                

socketIO.on('pushState', on_push_state)

# get initial state
socketIO.emit('getState', '', on_push_state)

try:
	socketIO.wait()
except KeyboardInterrupt:
	pass
