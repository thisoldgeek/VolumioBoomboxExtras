#!/usr/bin/env python

import RPi.GPIO as GPIO
import lirc
import time
from time import sleep
import spidev
import VFD

GPIO.setmode(GPIO.BCM)
neopixel_GPIO = 17        # High on this pin tells Arduino 'lights on", Low is 'lights off'
music_display= 0          # toggle this variable to tell arduino to show light effects for music
                          # you can't read an output directly, so read the variable and set the output
GPIO.setup(neopixel_GPIO, GPIO.OUT, initial=GPIO.LOW)
   
# Turn NeoPixels on/off
music_display= 0          # toggle this variable to tell arduino to show light effects for music

# initalize SPI
vfd=VFD.SPI()

#vfd.init_VFD()

# Toggle LED Matrix and NeoPixels on and off based on 'back' button 
def lights_to_music():  
        global music_display
        if music_display:  # if music effects are on, turn them off
           GPIO.output(neopixel_GPIO, False)
           music_display = False
           print "turning LEDs off"
        else: 
           GPIO.output(neopixel_GPIO, True)        # if music effects are OFF, turn them on
           music_display = True
           print "turning LEDs ON!"


while True:
    sockid = lirc.init("irexec")
    code = lirc.nextcode()
    ir_cmd = [x.encode('ascii') for x in code]
    if len(ir_cmd) > 0:
        if ir_cmd[0] == 'back':
           lights_to_music()
        elif ir_cmd[0] == 'bright':
             vfd.brightnessAdjust()
             print("VFD Brightness")
    lirc.deinit()
    sleep(0.25)

