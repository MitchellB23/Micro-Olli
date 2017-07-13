#*******************************************************
#* Copyright (C) 2017 Mitchell Beard
#*************manual Drive and collection**********
# Uses a Raspi, Servo, Tallons, and cim motors to control Micro Olli and  collect data****
# This will move channel 0 from min to max position repeatedly.
# Controls:
# 	w:	Move forward
#	a:	Turn left
#	d:	Turn right
#	s:	Move back
#	z: 	Exit
from __future__ import division
import time
import os, os.path

# Import the PCA9685 module.
import Adafruit_PCA9685
import sys	#Used for closing the running program
import pygame #Gives access to KEYUP/KEYDOWN events
import picamera

#Initialization for pygame
pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Remote Control Window')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

# Display some text
instructions = '''
    Micro Olli V2 Controls
    
    Press:
    ->w: Move GoPiGo Robot forward
    ->a: Turn GoPiGo Robot left
    ->d: Turn GoPiGo Robot right
    ->s: Move GoPiGo Robot backward
    ->z: Exit
    ''';
size_inc=15
index=0
for i in instructions.split('\n'):
    font = pygame.font.Font(None, 36)
        text = font.render(i, 1, (10, 10, 10))
        background.blit(text, (10,10+size_inc*index))
        index+=1

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 100  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

imageinxa=len([name for name in os.listdir('/home/pi/Desktop/GoPiGolocal/Data/a') if os.path.isfile(os.path.join('/home/pi/Desktop/GoPiGolocal/Data/a',name))])#define a

imageinxw=len([name for name in os.listdir('/home/pi/Desktop/GoPiGolocal/Data/w') if os.path.isfile(os.path.join('/home/pi/Desktop/GoPiGolocal/Data/w',name))])#define w

imageinxd=len([name for name in os.listdir('/home/pi/Desktop/GoPiGolocal/Data/d') if os.path.isfile(os.path.join('/home/pi/Desktop/GoPiGolocal/Data/d',name))])#define d

while True:
    event = pygame.event.wait();
        if (event.type == pygame.KEYUP):
            pwm.set_pwm(0, 0, 0)
            pwm.set_pwm(1, 0, 0)
                continue;
        if (event.type != pygame.KEYDOWN):
            continue;
        char = event.unicode;
        if char=='w':
            imagename='/home/pi/Desktop/GoPiGolocal/Data/'+char+'/'+str(imageinxw)+'.jpg' #names image
            imageinxw=imageinxw+1
            camera.capture(imagename)#takes picture
            pwm.set_pwm(0, 0, 450)
            pwm.set_pwm(1, 0, 450) #Move forward
                print('forward')
        elif char=='a':
            imagename='/home/pi/Desktop/GoPiGolocal/Data/'+char+'/'+str(imageinxa)+'.jpg'
            imageinxa=imageinxa+1
            camera.capture(imagename)
            pwm.set_pwm(0, 0, 500) # Move left
            pwm.set_pwm(1, 0, 325)
                print('left')
        elif char=='d':
            imagename='/home/pi/Desktop/GoPiGolocal/Data/'+char+'/'+str(imageinxd)+'.jpg'
            imageinxd=imageinxd+1
            camera.capture(imagename)
            pwm.set_pwm(1, 0, 500) #Move right
            pwm.set_pwm(0, 0, 325)
                print('right')
        elif char=='s':
            pwm.set_pwm(1, 0, 350) #Move backward
            pwm.set_pwm(0, 0, 350)
                print('backward')
elif char=='z':
    print ("\nExiting"); #Exit
        sys.exit();
