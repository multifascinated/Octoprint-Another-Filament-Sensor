#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

print("doing a filament test")
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  switch_state = GPIO.input(4)
  print('Switch value: '+str(switch_state))
  time.sleep(2)

print('Exiting')
