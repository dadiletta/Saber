#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import bluetooth

#BCM is different numbering than BOARD. Google it
GPIO.setmode(GPIO.BCM)

# init list with pin numbers
# This makes changing pins less of a chore
pinList = [14]

# loop through pins and set mode and state to 'high'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop
SleepTimeL = 15

#counter to double check bluetooth before cutting power
count = 0

# main loop
try:
  while True:
    result = bluetooth.lookup_name('08:ec:a9:0f:88:3e', timeout=5)
    if(result != None):
        print "I see Mr. A!"
        GPIO.output(pinList[0], GPIO.HIGH)
        print str(pinList[0]) + " set to high"
        count = 0
    else:
        #we see the bluetooth missing once
        count += 1;
        if count > 1:
        GPIO.output(pinList[0], GPIO.LOW)
    #break between cycles
    time.sleep(SleepTimeL)

  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A