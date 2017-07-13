#*******************************************************
#* Copyright (C) 2017 Mitchell Beard
#* This file is part of MicroOlli.
#************************************************
#*****************client the runs on olli wile server also runs to make Olli drive autonomously
import socket               # Import socket module
from gopigo import *	#Has the basic functions for controlling the GoPiGo Robot
import sys	#Used for closing the running program
import pygame #Gives access to KEYUP/KEYDOWN events
import picamera
import os, os.path
import numpy as np
import argparse
import os
import sys
pwm = Adafruit_PCA9685.PCA9685()
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
# Import the PCA9685 module.
pwm.set_pwm_freq(60)
import Adafruit_PCA9685
camera=picamera.PiCamera()
charpre='p'
accelerate=0

if __name__ == '__main__':
    iteration=0
    while True:
        imagename='/home/pi/Desktop/capture.jpg'
        camera.capture(imagename)
        s = socket.socket()         # Create a socket object
        host = '192.168.1.15' # Get local machine name
        port = 12344                 # Reserve a port for your service.

        
        s.connect((host, port))
        f = open('capture.jpg','rb')
        print 'Sending...'
        l = f.read(1024)
        while (l):
            print 'Sending...'
            s.send(l)
            l = f.read(1024)
        f.close()
        print "Done Sending"
        s.shutdown(socket.SHUT_WR)

        
        char=s.recv(1024)
        print('character received is ',char)
        s.close()

        if char=='w':
                    pwm.set_pwm(0, 1, 450)
                    pwm.set_pwm(1, 1, 450) #Move forward
                    print('forward')
                    time.sleep(.5)
                    pwm.set_pwm(0, 1, 0)
                    pwm.set_pwm(1, 1, 0)
        elif char=='a':
                    pwm.set_pwm(1, 0, 500) # Move left
                    pwm.set_pwm(0, 0, 325)
                    print('left')

                    time.sleep(0.5)
                    
                    pwm.set_pwm(0, 1, 450)
                    pwm.set_pwm(1, 1, 450)

                    time.sleep(0.5)

                    pwm.set_pwm(0, 1, 0)
                    pwm.set_pwm(1, 1, 0)



                    print('running in a')
                    
                     
                    
        elif char=='d':
                    #right();# Turn Right
                    pwm.set_pwm(0, 0, 500) # Move left
                    pwm.set_pwm(1, 0, 325)
                    print('left')
                    
                    time.sleep(0.5)
                    
                    pwm.set_pwm(0, 1, 450)
                    pwm.set_pwm(1, 1, 450)
                    
                    time.sleep(0.5)
                    
                    pwm.set_pwm(0, 1, 0)
                    pwm.set_pwm(1, 1, 0)
                    
                    
                    
            print('running in a')
                  
                    
        elif char=='s':
                    pwm.set_pwm(1, 0, 350) #Move backward
                    pwm.set_pwm(0, 0, 350)
                    print('backward')
        
        elif char=='t':
                    increase_speed();	# Increase speed
                    print('running in t')
        elif char=='g':
                    decrease_speed();	# Decrease speed
                    print('running in g')
           
            
        if (charpre==char) and (charpre=='a' or charpre=='d'):
               accelerate=accelerate+5
        else:
               accelerate=0
        charpre=char
        print('acceleration is ',accelerate)
        iteration=iteration+1



        
