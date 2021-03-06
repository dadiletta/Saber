'''
## License
The MIT License (MIT)
GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

from grovepi import *
from grove_rgb_lcd import *
import grovepi
import time
import requests
import Private
import random
import tkinter


# Configure buzzer on D4
buzzer = 4
grovepi.pinMode(buzzer,"OUTPUT")

# Connect the Grove LED to digital port D7-8
gled = 7
rled = 8
grovepi.pinMode(gled,"OUTPUT")
grovepi.pinMode(rled,"OUTPUT")

# Connect the Grove Ultrasonic Ranger to digital port D2
ultrasonic_ranger = 2

# Connect the Grove Button to digital port D3
button = 3
grovepi.pinMode(button,"INPUT")

# Connect the Grove Temperature Sensor to analog port A0
sensor = 0

# Connect the Grove Rotary Angle Sensor to analog port A1
potentiometer = 1
time.sleep(1)
### Reference voltage of ADC is 5v
adc_ref = 5
### Vcc of the grove interface is normally 5v
grove_vcc = 5
### Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

#This is how I'm trying to safely include my IFTTT key to the Maker channel
MAKER_SECRET = Private.Private.MAKER_SECRET


########################
##WELCOME TO SABER CLASS
########################
class Saber:
    
    root = Tk()
    root.title("TheLanceVote")


    def __init__(self):
        print "Saber instantiated."
        

    
    ######################
    ######################
    ### GUI
    ######################
    ######################  
    
    def calculate(*args):
        try:
            value = float(feet.get())
            meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass
    
    ######################
    ######################
    ### DEMOS
    ######################
    ######################

        
    ############
    #LCD demo
    ############    
    def demoLCD(self):
        setText("Hello world\nLCD test")
        setRGB(0,128,64)
        
        for c in range(0,255):
            setRGB(c,255-c,0)
            time.sleep(0.01)
        
        setRGB(0,255,0)
        setText("Bye bye, this should wrap")
        
        
    ############
    #Temp demo
    ############
    def demoTemp(self):
        while True:
            try:
                temp = grovepi.temp(sensor,'1.1')
                print("temp =", temp)
                time.sleep(.5)
        
            except KeyboardInterrupt:
                break
            except IOError:
                print ("Error")

    ############
    #Buzzer demo
    ############              
    def demoBuzzer(self):
        while True:
            try:
                # Buzz for 1 second
                grovepi.digitalWrite(buzzer,1)
                print ('start')
                time.sleep(1)
        
                # Stop buzzing for 1 second and repeat
                grovepi.digitalWrite(buzzer,0)
                print ('stop')
                time.sleep(1)
        
            except KeyboardInterrupt:
                grovepi.digitalWrite(buzzer,0)
                break
            except IOError:
                print ("Error")


    ############
    #Button demo
    ############    
    def demoButton(self):
        while True:
            try:
                print(grovepi.digitalRead(button))
                time.sleep(.5)
        
            except IOError:
                print ("Error")
            except KeyboardInterrupt:
                break

    ############
    #LED demo
    ############   
    def demoLED(self):
        while True:
            try:
                #Blink the LED
                digitalWrite(gled,1)		# Send HIGH to switch on LED
                print "Green ON!"
                digitalWrite(rled,0)
                time.sleep(1)

                digitalWrite(gled,0)		# Send LOW to switch off LED
                digitalWrite(rled,1)
                print "Green OFF!"
                time.sleep(1)

            except KeyboardInterrupt:	# Turn LED off before stopping
                digitalWrite(gled,0)
                break
            except IOError:				# Print "Error" if communication error encountered
                print ("Error")
            except KeyboardInterrupt:
                digitalWrite(rled,0)
                digitalWrite(gled,0)
                break

    ############
    #US_Range demo
    ############  
    def demoRange(self):
        while True:
            try:
                # Read distance value from Ultrasonic
                print (grovepi.ultrasonicRead(ultrasonic_ranger))

            except TypeError:
                print ("Error")
            except IOError:
                print ("Error")
            except KeyboardInterrupt:
                break

    ############
    #Knob demo
    ############  
    def demoKnob(self):
        while True:
            try:
                # Read sensor value from potentiometer
                sensor_value = grovepi.analogRead(potentiometer)
        
                # Calculate voltage
                voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
        
                # Calculate rotation in degrees (0 to 300)
                degrees = round((voltage * full_angle) / grove_vcc, 2)
        
                # Calculate LED brightess (0 to 255) from degrees (0 to 300)
                brightness = int(degrees / full_angle * 255)
        
                # Give PWM output to LED
                grovepi.analogWrite(gled,brightness)
        
                print("sensor_value = %d voltage = %.2f degrees = %.1f brightness = %d" %(sensor_value, voltage, degrees, brightness))
            except KeyboardInterrupt:
                grovepi.analogWrite(gled,0)
                break
            except IOError:
                print ("Error")
                
                
    ############
    #Maker channel demo
    ############                  
    def demoMaker(self):
        
        print("Sending dark mode trigger.")
        payload = "{ 'value1' : 'hello', 'value2' : 'hello', 'value3' : 'hello'}" 
        requests.post("https://maker.ifttt.com/trigger/demoMaker/with/key/"+MAKER_SECRET, data=payload)
        
    ######################
    ######################
    ### LOGIC
    ######################
    ######################
    
    ############
    #Menu display and selection
    ############     
    def formMenu(self, items):
        itemRange = int(1000/len(items))
        while True:
            try:
                # Read sensor value from potentiometer
                sensor_value = grovepi.analogRead(potentiometer)
                selection = int(sensor_value/itemRange)
                # check to make sure that our index value isn't going over
                if selection >= len(items):
                    selection = len(items) - 1
                setText(list(items[selection]))
                self.colorSelect(selection)
                
                if grovepi.digitalRead(button) == 1:
                    self.clear()
                    return selection
                
                time.sleep(0.5)
            except KeyboardInterrupt:
                grovepi.analogWrite(gled,0)
                break
            except IOError:
                print ("Error")

    ############
    #Returns colors based on index
    ############ 
    def colorSelect(self, x):
            if x == 0:
                setRGB(255, 255, 255)
            elif x == 1:
                setRGB(205, 0, 0)
            elif x == 2:
                setRGB(0, 205, 0)
            elif x == 3:
                setRGB(0, 0, 205)
            elif x == 4:
                setRGB(205, 0, 205)
            elif x == 5:
                setRGB(150, 255, 255)
            elif x == 6:
                setRGB(255, 178, 102)
            else:
                setRGB(100, 0, 200)

    ############
    #Launch GUI
    ############ 
    def launchGUI(self):
        root = Tk()
        root.title("Feet to Meters")
        
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        
        feet = StringVar()
        meters = StringVar()
        
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        
        ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
        
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
        
        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        
        feet_entry.focus()
        root.bind('<Return>', calculate)
        
        root.mainloop()
    ############
    #Sensor in box checks if something (box's lid) is right 
    #Above. Triggers alarm if opened. Button disables
    ############ 
    def coverCheck(self):
        counter = 0
        while True:
            try:
                dist = grovepi.ultrasonicRead(ultrasonic_ranger)
                print "DIST: " + str(dist) + " cm away."
                counter +=1
                if counter % 50 == 0 and dist > 500:
                    print "My cover is just sitting open, isn't it?"
                elif dist > 50:
                    try:
                        #Blink the LED
                        digitalWrite(rled,1)		# Send HIGH to switch on LED
                        digitalWrite(buzzer,1)
                        print "Hey!"
                        time.sleep(1)

                        digitalWrite(rled,0)		# Send LOW to switch off LED
                        digitalWrite(buzzer,0)
                        print "Close the lid."
                        time.sleep(1)

                    except IOError:				# Print "Error" if communication error encountered
                        print ("Error")
            except TypeError:
                print ("Error")
            except IOError:
                print ("Error")
            except KeyboardInterrupt:
                digitalWrite(rled,0)
                digitalWrite(buzzer,0)
                break

    ############
    ## CLEAR
    ############
    def clear(self):
        digitalWrite(rled,0)
        digitalWrite(buzzer,0)
        digitalWrite(gled,0)
        
        setText("")
        setRGB(0,0,0)
        
    #############
    ### RootMenu
    #############
    def rootMenu(self):
        root = ["Function Demos", "Light Settings", "Phone Options"]
        light = ["All off", "All on", "Work mode", "Movie mode", "Bed chill"]
        people = ["Dan", "Laura", "MamaMarti", "MamaSusan"]
        choice = self.formMenu(root)
        if selection == 1:
            self.formMenu(light)
        elif selection == 2:
            self.formMenu(people)
            
            
