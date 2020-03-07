#!/usr/bin/env python

import RPi.GPIO as GPIO
import lirc
import time
from time import sleep
import spidev
import VFD

GPIO.setmode(GPIO.BCM)
music_display= 0          # toggle this variable to tell arduino to show light effects for music
                          # you can't read an output directly, so read the variable and set the output
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

sockid = lirc.init("irexec","/home/volumio/VolumioBoomboxExtras/lircrc")
   
# Turn NeoPixels on/off
music_display= 0          # toggle this variable to tell arduino to show light effects for music

# initalize SPI
vfd=VFD.SPI()

vfd.init_VFD()

# Toggle LED Matrix and NeoPixels on and off based on 'back' button 
def lights_to_music():  
        global music_display
        if music_display:  # if music effects are on, turn them off
           GPIO.output(24, False)
           music_display = False
           print "turning LEDs off"
        else: 
           GPIO.output(24, True)        # if music effects are OFF, turn them on
           music_display = True
           print "turning LEDs ON!"


while True:
   button = lirc.nextcode()

   if len(button) <> 0:
      #print ("Getting button")
      print button[0]
      if button[0] == "back":
         lights_to_music()
      elif button[0] == "bright":
         vfd.brightnessAdjust()
  
