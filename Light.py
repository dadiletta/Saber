from grovepi import *

# Connect the Grove LED to digital port D4
led = 4

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 5

class Saber:

    def __init__(self):
        print "Saber initialized."

    def blink(self):
        while True:
            try:
                #Blink the LED
                digitalWrite(led,1)		# Send HIGH to switch on LED
                print "LED ON!"
                time.sleep(1)

                digitalWrite(led,0)		# Send LOW to switch off LED
                print "LED OFF!"
                time.sleep(1)

            except KeyboardInterrupt:	# Turn LED off before stopping
                digitalWrite(led,0)
                break
            except IOError:				# Print "Error" if communication error encountered
                print ("Error")


    def distance(self):
        while True:
                try:
                    # Read distance value from Ultrasonic
                    print (grovepi.ultrasonicRead(ultrasonic_ranger))

                except TypeError:
                    print ("Error")
                except IOError:
                    print ("Error")
