import Light

__author__ = 'adilettad'


print("---------------")
print("----Welcome----")
print("------to-------")
print("-----Saber-----")
print("---------------")
sab = Light.Saber()

while True:

    command = raw_input('Your command:')

    if command == "blink":
        sab.demoLED()
    elif command == "dist" or command == "range":
        sab.demoRange()
    elif command == "watch" or command == "cover":
        sab.coverCheck()
    elif command =="knob":
        sab.demoKnob()
    elif command =="lcd":
        sab.demoLCD()
    elif command =="temp":
        sab.demoTemp()
    elif command =="buzzer":
        sab.demoBuzzer()
    elif command =="button":
        sab.demoButton()
    elif command =="clear":
        sab.clear()
    elif command =="maker":
        sab.demoMaker()
    elif command =="menu":
        exampleMenu = ["One", "Two", "Three", "Four", "Five"]
        print(sab.formMenu(exampleMenu)+1)

    ##Need Ctrl+C protection on all methods

